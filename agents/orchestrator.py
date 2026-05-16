"""OrchestratorAgent — direct Python pipeline coordinator with crash recovery."""
from __future__ import annotations

import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from config import PROCESSED_DIR, REGIONS
from agents.scraper_agent import ScraperAgent
from agents.summarizer_agent import SummarizerAgent
from agents.breaking_news_agent import BreakingNewsAgent

console = Console()

# Parallel workers — 4 keeps us well under Anthropic's concurrent-request limit
_MAX_WORKERS = 4


class OrchestratorAgent:
    """Drives the full daily news pipeline with per-region result persistence."""

    def __init__(self) -> None:
        self._scraper    = ScraperAgent()
        self._summarizer = SummarizerAgent()
        self._breaking   = BreakingNewsAgent()

        self.region_summaries: dict[str, dict] = {}
        self.all_articles: list[dict] = []
        self.breaking_events: list[dict] = []
        self._lock = threading.Lock()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_pipeline(self, resume: bool = False) -> dict:
        today = date.today().isoformat()
        day_dir = PROCESSED_DIR / today
        day_dir.mkdir(parents=True, exist_ok=True)

        console.rule(f"[bold cyan]News Agent Pipeline — {today}")

        # ── Step 1: Scrape + Summarize regions in parallel ────────────
        with ThreadPoolExecutor(max_workers=_MAX_WORKERS) as pool:
            futures = {
                pool.submit(self._process_region, region, day_dir, today, resume): region
                for region in REGIONS
            }
            for future in as_completed(futures):
                region = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    console.log(f"[red]✗ {region.upper()} failed: {exc}[/red]")

        # ── Step 2: Breaking news across all regions ──────────────────
        breaking_path = day_dir / "breaking.json"

        if resume and breaking_path.exists():
            console.log("[dim]▶ Breaking News — loaded from cache[/dim]")
            self.breaking_events = json.loads(breaking_path.read_text(encoding="utf-8"))
        else:
            console.log("\n[magenta bold]▶ Breaking News Detection[/magenta bold]")
            self.breaking_events = self._breaking.detect(self.region_summaries, today)
            console.log(f"  [green]✓[/green] {len(self.breaking_events)} breaking event(s) detected")
            breaking_path.write_text(
                json.dumps(self.breaking_events, ensure_ascii=False, indent=2), encoding="utf-8"
            )

        console.print(Panel.fit(
            f"[green]Pipeline complete[/green] · "
            f"{len(self.region_summaries)} regions · "
            f"{len(self.all_articles)} articles · "
            f"{len(self.breaking_events)} breaking events",
            border_style="green",
        ))

        return {
            "date": today,
            "region_summaries": self.region_summaries,
            "breaking_events":  self.breaking_events,
        }

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _process_region(self, region: str, day_dir: Path, today: str, resume: bool) -> None:
        """Scrape + summarize one region; safe to run in a thread."""
        summary_path = day_dir / f"{region}.json"

        if resume and summary_path.exists():
            console.log(f"[dim]▶ {region.upper()} — loaded from cache[/dim]")
            digest = json.loads(summary_path.read_text(encoding="utf-8"))
            raw_path = day_dir / f"{region}_raw.json"
            articles: list[dict] = []
            if raw_path.exists():
                articles = json.loads(raw_path.read_text(encoding="utf-8"))
            with self._lock:
                self.region_summaries[region] = digest
                self.all_articles.extend(articles)
            return

        console.log(f"[yellow bold]▶ {region.upper()}[/yellow bold]")

        articles = self._scraper.scrape_region(region)
        for a in articles:
            a["region"] = region
        console.log(f"  [green]✓[/green] {region.upper()} scraped {len(articles)} articles")

        raw_path = day_dir / f"{region}_raw.json"
        raw_path.write_text(json.dumps(articles, ensure_ascii=False, indent=2), encoding="utf-8")

        digest = self._summarizer.summarize_region(region, articles, today)
        console.log(f"  [green]✓[/green] {region.upper()} summarized → {len(digest.get('stories', []))} stories")

        summary_path.write_text(json.dumps(digest, ensure_ascii=False, indent=2), encoding="utf-8")

        with self._lock:
            self.region_summaries[region] = digest
            self.all_articles.extend(articles)
