"""Shared base class for all Claude-backed agents."""
from __future__ import annotations

import json
import time
from abc import ABC, abstractmethod
from typing import Any

import anthropic
from rich.console import Console

from config import ANTHROPIC_API_KEY

console = Console()


class _StopAgent(Exception):
    """Raised by _dispatch_tool to signal the agent loop should terminate early."""


class BaseAgent(ABC):
    """Drives a Claude model through an agentic tool-use loop with retry on rate limits."""

    def __init__(self, model: str, system_prompt: str, tools: list[dict],
                 max_tokens: int = 4096) -> None:
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self.model = model
        self.system_prompt = system_prompt
        self.tools = tools
        self.max_tokens = max_tokens

    # ------------------------------------------------------------------
    # Core agentic loop
    # ------------------------------------------------------------------

    def run(self, user_message: str, **kwargs: Any) -> Any:
        """Run the agent to completion and return the final parsed result."""
        messages: list[dict] = [{"role": "user", "content": user_message}]

        while True:
            response = self._create_with_retry(messages)

            # Convert SDK content blocks → plain dicts to avoid Pydantic
            # serialisation mismatches on subsequent API calls.
            assistant_content = _blocks_to_dicts(response.content)
            messages.append({"role": "assistant", "content": assistant_content})

            if response.stop_reason == "end_turn":
                for block in response.content:
                    if hasattr(block, "text"):
                        return self._parse_result(block.text)
                return None

            if response.stop_reason == "tool_use":
                tool_results: list[dict] = []
                early_stop = False

                for block in response.content:
                    if block.type != "tool_use":
                        continue
                    console.log(f"[dim][{self.__class__.__name__}] tool → {block.name}[/dim]")
                    try:
                        result = self._dispatch_tool(block.name, block.input)
                    except _StopAgent:
                        early_stop = True
                        result = {"status": "stopped"}

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result, ensure_ascii=False),
                    })

                if early_stop:
                    return self._parse_result("")

                messages.append({"role": "user", "content": tool_results})

    # ------------------------------------------------------------------
    # Rate-limit retry wrapper
    # ------------------------------------------------------------------

    def _create_with_retry(self, messages: list[dict], max_retries: int = 4) -> Any:
        """Call messages.create with exponential backoff on 429 rate-limit errors."""
        delay = 60  # start with a full-minute wait
        for attempt in range(max_retries):
            try:
                kwargs: dict = dict(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self.system_prompt,
                    messages=messages,
                )
                if self.tools:
                    kwargs["tools"] = self.tools
                return self.client.messages.create(**kwargs)
            except anthropic.RateLimitError:
                if attempt == max_retries - 1:
                    raise
                console.log(
                    f"[yellow][{self.__class__.__name__}] rate limit — "
                    f"waiting {delay}s (attempt {attempt+1}/{max_retries})[/yellow]"
                )
                time.sleep(delay)
                delay = min(delay * 2, 300)  # cap at 5 min
        raise RuntimeError("Unreachable")

    # ------------------------------------------------------------------
    # Subclass hooks
    # ------------------------------------------------------------------

    @abstractmethod
    def _dispatch_tool(self, name: str, inputs: dict) -> Any:
        """Route a tool-use call to the appropriate implementation.
        May raise _StopAgent to terminate the loop early."""

    def _parse_result(self, text: str) -> Any:
        """Override to post-process Claude's final text response."""
        t = (text or "").strip()
        if t.startswith("```"):
            t = t.split("\n", 1)[-1]
            t = t.rsplit("```", 1)[0].strip()
        try:
            return json.loads(t)
        except (json.JSONDecodeError, TypeError):
            return text


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _blocks_to_dicts(blocks) -> list[dict]:
    """Convert Anthropic SDK content-block objects to plain serialisable dicts."""
    result = []
    for block in blocks:
        if block.type == "text":
            result.append({"type": "text", "text": block.text})
        elif block.type == "tool_use":
            result.append({
                "type":  "tool_use",
                "id":    block.id,
                "name":  block.name,
                "input": block.input,
            })
        elif hasattr(block, "model_dump"):
            result.append(block.model_dump())
    return result
