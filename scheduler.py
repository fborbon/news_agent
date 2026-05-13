"""APScheduler wrapper — runs the news pipeline daily."""
from __future__ import annotations

import signal
import sys
from typing import Callable

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from rich.console import Console

from config import SCHEDULE_HOUR, SCHEDULE_MINUTE

console = Console()


def start_scheduler(pipeline_fn: Callable[[], None]) -> None:
    """Block forever, calling pipeline_fn once daily at the configured time."""
    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(
        pipeline_fn,
        trigger=CronTrigger(hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE),
        id="daily_news_pipeline",
        name="Daily News Pipeline",
        misfire_grace_time=3600,  # tolerate up to 1h late start
    )

    console.print(
        f"[cyan]Scheduler started[/cyan] — next run at "
        f"[bold]{SCHEDULE_HOUR:02d}:{SCHEDULE_MINUTE:02d} UTC[/bold] daily. "
        "Press Ctrl+C to stop."
    )

    def _shutdown(sig, frame):
        console.print("\n[yellow]Shutting down scheduler…[/yellow]")
        scheduler.shutdown(wait=False)
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    scheduler.start()
