"""ScraperAgent — direct Python RSS ingestion + article extraction.

No Claude agent loop here: scraping is pure I/O work, not reasoning.
Claude is kept for summarisation and breaking-news analysis where it adds value.
"""
from __future__ import annotations

import feedparser
import httpx
import trafilatura
from rich.console import Console

from config import MAX_ARTICLES_PER_SOURCE, MAX_ARTICLE_CHARS, RSS_TIMEOUT
from sources.news_sources import NEWS_SOURCES

console = Console()

# How many articles per source to fetch full content for (RSS summary used for rest)
FULL_CONTENT_LIMIT = 5


class ScraperAgent:
    """Fetches RSS feeds and extracts article text for a given region."""

    def scrape_region(self, region: str) -> list[dict]:
        sources = NEWS_SOURCES.get(region, [])
        articles: list[dict] = []
        for source in sources:
            console.log(f"  [dim]  ↳ {source['name']} …[/dim]")
            feed_items = self._fetch_rss(source)
            for i, item in enumerate(feed_items[:MAX_ARTICLES_PER_SOURCE]):
                if i < FULL_CONTENT_LIMIT and item.get("url"):
                    item["content"] = self._extract_content(item["url"])
                # Fall back to RSS summary if extraction failed or skipped
                if not item.get("content"):
                    item["content"] = item.get("summary", "")
                item["region"] = region
                item["source_home"] = source.get("home", "")
                articles.append(item)
        return articles

    # ------------------------------------------------------------------

    def _fetch_rss(self, source: dict) -> list[dict]:
        url, name = source["rss"], source["name"]
        try:
            feed = feedparser.parse(
                url, request_headers={"User-Agent": "NewsAgent/1.0"}
            )
            items = []
            for entry in feed.entries[:MAX_ARTICLES_PER_SOURCE]:
                items.append({
                    "title":     entry.get("title", "").strip(),
                    "source":    name,
                    "url":       entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary":   entry.get("summary", "")[:800],
                    "content":   "",
                })
            return items
        except Exception as exc:
            console.log(f"[red]    RSS error [{name}]: {exc}[/red]")
            return []

    def _extract_content(self, url: str) -> str:
        try:
            with httpx.Client(
                timeout=RSS_TIMEOUT,
                follow_redirects=True,
                headers={"User-Agent": "NewsAgent/1.0"},
            ) as client:
                resp = client.get(url)
                resp.raise_for_status()
                html = resp.text
            text = trafilatura.extract(
                html, include_comments=False, include_tables=False
            ) or ""
            return text[:MAX_ARTICLE_CHARS]
        except Exception:
            return ""
