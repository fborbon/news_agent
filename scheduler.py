"""APScheduler wrapper — runs the news pipeline daily."""
from __future__ import annotations

import signal
import sys
from typing import Callable

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from rich.console import Console

from config import SCHEDULE_TIMES

console = Console()


def start_scheduler(pipeline_fn: Callable[[], None]) -> None:
    """Block forever, calling pipeline_fn three times daily at the configured times."""
    scheduler = BlockingScheduler(timezone="UTC")
    for hour, minute in SCHEDULE_TIMES:
        scheduler.add_job(
            pipeline_fn,
            trigger=CronTrigger(hour=hour, minute=minute),
            id=f"news_pipeline_{hour:02d}{minute:02d}",
            name=f"News Pipeline {hour:02d}:{minute:02d} UTC",
            misfire_grace_time=3600,
        )

    times_str = "  ·  ".join(f"{h:02d}:{m:02d}" for h, m in SCHEDULE_TIMES)
    console.print(
        f"[cyan]Scheduler started[/cyan] — runs at "
        f"[bold]{times_str} UTC[/bold] daily. "
        "Press Ctrl+C to stop."
    )

    def _shutdown(sig, frame):
        console.print("\n[yellow]Shutting down scheduler…[/yellow]")
        scheduler.shutdown(wait=False)
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    scheduler.start()
