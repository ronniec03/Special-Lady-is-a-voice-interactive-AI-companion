"""Skeleton adapter for Interactive Brokers using TWS or IB Gateway."""
from __future__ import annotations

import asyncio
from typing import Any, Dict, AsyncIterator

from .base import BrokerAdapter


class IBKRAdapter(BrokerAdapter):
    def __init__(self, host: str = "127.0.0.1", port: int = 7497, client_id: int = 1) -> None:
        self.host = host
        self.port = port
        self.client_id = client_id
        self._connected = asyncio.Event()

    async def connect(self) -> None:
        """Connect to the TWS/Gateway instance.

        Actual implementation should leverage `ib_insync` or the official API.
        """
        # TODO: implement real connection logic
        self._connected.set()

    async def place_order(self, order: Dict[str, Any]) -> str:
        await self._connected.wait()
        # TODO: translate and submit order via IB API
        return "IBKR_ORDER_ID"

    async def stream_quotes(self, symbol: str) -> AsyncIterator[Dict[str, Any]]:
        await self._connected.wait()
        while True:
            # TODO: replace with real market data stream
            yield {"symbol": symbol, "bid": 0.0, "ask": 0.0}
            await asyncio.sleep(1)
