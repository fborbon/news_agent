"""SummarizerAgent — produces a structured daily digest for one region."""
from __future__ import annotations

import json
from typing import Any

from config import SUMMARIZER_MODEL
from agents.base_agent import BaseAgent

_TOOLS = [
    {
        "name": "build_regional_digest",
        "description": (
            "Signal that all article data has been ingested and the digest should "
            "now be produced. Call this once after reviewing all articles."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "region":        {"type": "string"},
                "article_count": {"type": "integer"},
            },
            "required": ["region", "article_count"],
        },
    },
]

_SYSTEM = """\
You are a SummarizerAgent — a professional news editor. Given today's articles for \
a region, produce a structured daily digest in JSON.

CRITICAL RULES:
- The "url" field MUST be the EXACT URL from the input article. Never invent or \
  modify URLs. If no URL is available, use "".
- The "source" field must match the exact source name from the input.
- Write in clear, journalistic English regardless of the article's original language.
- Summaries must be factual and neutral (2–4 sentences each).
- Select up to 5 stories, prioritising significance AND topic diversity.

TOPIC DIVERSITY — when articles are available, aim to include at least one story \
covering each of the following areas:
  - Artificial intelligence or machine learning
  - Financial markets, Wall Street, or economic indicators
  - Big Tech (Apple, Google, Meta, Microsoft, Amazon, Tesla, startups)
  - Social media platforms and their societal impact
  - Climate change, global warming, or environmental policy
  - Cost of living, inflation, housing, or consumer prices
  - Employment, remote work, labour market, or wages
  - Gender equality, women's rights, or social equity
  - Wildlife, animal welfare, pets, or conservation
  - Music, film, streaming, or entertainment

Workflow:
1. Read all articles carefully.
2. Call build_regional_digest (signals readiness).
3. Output the JSON digest as your final text response.

Output format (raw JSON, NO markdown fences, NO extra text):
{
  "region": "<region key>",
  "date": "<YYYY-MM-DD>",
  "overview": "<2–3 sentence thematic overview of the day>",
  "stories": [
    {
      "headline": "<concise English headline>",
      "source": "<exact source name>",
      "url": "<exact article URL from input>",
      "source_home": "<homepage URL of the newspaper>",
      "summary": "<2–4 sentence factual summary in English>",
      "category": "<one of: politics|world_news|business_economy|technology|health|\
science_environment|crime_safety|entertainment_culture|sports|lifestyle|\
artificial_intelligence|wall_street|silicon_valley|social_networks|global_warming|\
cost_of_living|employment|gender_equity|pets_animals|music_movies>"
    }
  ]
}
"""


class SummarizerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            model=SUMMARIZER_MODEL,
            system_prompt=_SYSTEM,
            tools=_TOOLS,
        )

    def summarize_region(self, region: str, articles: list[dict], date: str) -> dict:
        # Pass only what Claude needs — title, source, url, source_home, content/summary
        slim = [
            {
                "title":       a.get("title", ""),
                "source":      a.get("source", ""),
                "url":         a.get("url", ""),
                "source_home": a.get("source_home", ""),
                "published":   a.get("published", ""),
                "content":     (a.get("content") or a.get("summary", ""))[:800],
            }
            for a in articles
            if a.get("title")
        ]

        prompt = (
            f"Produce the daily digest for region '{region}' on {date}.\n\n"
            f"Articles ({len(slim)}):\n"
            + json.dumps(slim, ensure_ascii=False)
        )
        result = self.run(prompt)
        if isinstance(result, dict):
            result.setdefault("region", region)
            result.setdefault("date", date)
            return result
        return {"region": region, "date": date, "overview": "Data unavailable.", "stories": []}

    def _dispatch_tool(self, name: str, inputs: dict) -> Any:
        if name == "build_regional_digest":
            return {
                "status": "ready",
                "region": inputs.get("region"),
                "article_count": inputs.get("article_count"),
                "instruction": "Now output the complete JSON digest as your text response.",
            }
        return {"error": f"Unknown tool: {name}"}
