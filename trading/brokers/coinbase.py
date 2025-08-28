"""Skeleton adapter for Coinbase Advanced Trade."""
from __future__ import annotations

import asyncio
import aiohttp
from typing import Any, Dict, AsyncIterator

from .base import BrokerAdapter


class CoinbaseAdapter(BrokerAdapter):
    BASE_URL = "https://api.exchange.coinbase.com"

    def __init__(self, api_key: str = "", api_secret: str = "", api_passphrase: str = "") -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self._session: aiohttp.ClientSession | None = None

    async def connect(self) -> None:
        headers = {"User-Agent": "trading-bot/0.1"}
        self._session = aiohttp.ClientSession(headers=headers)

    async def place_order(self, order: Dict[str, Any]) -> str:
        assert self._session, "Call connect() first"
        # TODO: implement signed REST request
        return "COINBASE_ORDER_ID"

    async def stream_quotes(self, symbol: str) -> AsyncIterator[Dict[str, Any]]:
        assert self._session, "Call connect() first"
        url = "wss://advanced-trade-ws.coinbase.com"  # placeholder
        async with self._session.ws_connect(url) as ws:
            # TODO: send subscription message
            while True:
                msg = await ws.receive_json()
                yield msg
                await asyncio.sleep(0)
