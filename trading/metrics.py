"""Expose Prometheus metrics for the trading system."""
from __future__ import annotations

from prometheus_client import Counter, Gauge, start_http_server

fills_total = Counter("fills_total", "Number of fills received")
open_orders = Gauge("open_orders", "Current open order count")


def start_metrics_server(port: int = 8000) -> None:
    start_http_server(port)
