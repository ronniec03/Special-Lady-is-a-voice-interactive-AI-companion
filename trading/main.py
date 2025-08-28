"""Entry point wiring together adapters, OMS, strategy and metrics."""
from __future__ import annotations

import asyncio

from .brokers.ibkr import IBKRAdapter
from .brokers.coinbase import CoinbaseAdapter
from .oms import OMS
from .strategy import ExampleStrategy
from .metrics import start_metrics_server, open_orders


async def main() -> None:
    ib = IBKRAdapter()
    cb = CoinbaseAdapter()
    await asyncio.gather(ib.connect(), cb.connect())

    oms = OMS(ib)
    strategy = ExampleStrategy(oms)

    start_metrics_server()
    await strategy.run()
    open_orders.set(len(await oms.list_open_orders()))


if __name__ == "__main__":
    asyncio.run(main())
