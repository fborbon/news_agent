"""BreakingNewsAgent — detects high-impact events and synthesises cross-source summaries.

Uses a single direct API call (no tool-use loop) so the token budget stays flat:
  - Input: ~8K tokens (200 digest stories, headline+url+source+region only)
  - Output: up to 8192 tokens (JSON array of breaking events)
  - No second turn, no accumulated context, no rate-limit cliff.

SummarizerAgent still showcases the tool-use / agentic pattern per-region.
"""
from __future__ import annotations

import json

import anthropic
from rich.console import Console

from config import ANTHROPIC_API_KEY, BREAKING_CATEGORIES, BREAKING_MODEL

console = Console()

_MAX_TOKENS = 16000  # 25 countries can produce 15+ events × ~1500 chars each

_SYSTEM = """\
You are a BreakingNewsAgent — a senior investigative editor specialising in high-impact events.

Breaking news categories you monitor:
- war_conflict               → active military conflicts, new wars, major escalations
- financial_collapse         → stock-market crashes, sovereign defaults, banking crises
- corporate_crisis           → Fortune-500 bankruptcies, major fraud or corporate scandals
- transportation_accident    → aviation, maritime, or rail disasters with mass casualties
- law_enforcement_operation  → counter-terrorism operations, large-scale raids, major arrests
- natural_disaster           → earthquakes, hurricanes, tsunamis, wildfires, catastrophic floods

CRITICAL RULES:
- The "url" field in each source object MUST be the exact URL from the input. Never invent URLs.
- The "name" field must be the exact source name from the input.
- Only report events with concrete, confirmed impact — not speculation or opinion.
- Group articles from different outlets that cover the SAME event into one entry.
- Include analysis of how different national sources frame the story differently.
- Report a MAXIMUM of 15 events, prioritising the most globally significant ones.

Return a raw JSON array (NO markdown fences, NO extra text):
[
  {
    "id": "<lowercase-hyphen-slug>",
    "category": "<category_key>",
    "title": "<clear event title>",
    "summary": "<3–5 sentence unified factual summary>",
    "analysis": "<1–2 sentences on how different sources frame the story>",
    "sources": [
      {
        "name": "<exact source name from input>",
        "url":  "<exact article URL from input>",
        "angle": "<brief framing note>"
      }
    ],
    "severity": "<critical|high|moderate>"
  }
]

Return [] (empty JSON array) if no qualifying breaking events are found.
"""


class BreakingNewsAgent:
    """Single-call breaking news detector — no tool-use loop, no multi-turn context."""

    def __init__(self) -> None:
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    def detect(self, region_summaries: dict[str, dict], date: str) -> list[dict]:
        """Detect breaking events from the regional digests in one API call."""

        # Compact payload: headline + url + source + region only (~40 tokens/story)
        # 25 regions × 8 stories = 200 items × 40 tokens ≈ 8K tokens total input
        stories = []
        for region, digest in region_summaries.items():
            for s in digest.get("stories", []):
                if s.get("headline"):
                    stories.append({
                        "headline": s.get("headline", ""),
                        "source":   s.get("source", ""),
                        "url":      s.get("url", ""),
                        "region":   region,
                        "summary":  s.get("summary", "")[:100],
                    })

        prompt = (
            f"Today is {date}. Analyse the {len(stories)} curated stories below "
            f"from {len(region_summaries)} country feeds. "
            "Identify high-impact breaking events, synthesise cross-source coverage, "
            "and return the JSON array.\n\n"
            "Stories:\n" + json.dumps(stories, ensure_ascii=False)
        )

        import time
        delay = 60
        for attempt in range(4):
            try:
                response = self.client.messages.create(
                    model=BREAKING_MODEL,
                    max_tokens=_MAX_TOKENS,
                    system=_SYSTEM,
                    messages=[{"role": "user", "content": prompt}],
                )
                break
            except Exception as exc:
                if "rate_limit" in str(exc).lower() and attempt < 3:
                    console.log(
                        f"[yellow][BreakingNewsAgent] rate limit — "
                        f"waiting {delay}s (attempt {attempt+1}/4)[/yellow]"
                    )
                    time.sleep(delay)
                    delay = min(delay * 2, 300)
                else:
                    raise

        text = ""
        for block in response.content:
            if hasattr(block, "text"):
                text = block.text.strip()
                break

        # Strip markdown fences if Claude added them despite instructions
        if text.startswith("```"):
            text = text.split("\n", 1)[-1]          # drop opening fence line
            text = text.rsplit("```", 1)[0].strip()  # drop closing fence

        try:
            result = json.loads(text)
            if isinstance(result, list):
                return result
        except (json.JSONDecodeError, TypeError):
            console.log(f"[red][BreakingNewsAgent] JSON parse failed — returning empty list[/red]")
        return []

    # Keep _dispatch_tool stub so this can still be imported by anything
    # that checks for it, though it's never called in single-call mode.
    def _dispatch_tool(self, name: str, inputs: dict):
        return {"error": "Not used in single-call mode"}
