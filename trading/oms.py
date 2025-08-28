"""Simple in-memory order management system with bracket order support."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Dict, Optional

from .brokers.base import BrokerAdapter


@dataclass
class Order:
    symbol: str
    side: str
    qty: float
    type: str = "market"
    limit: Optional[float] = None
    stop: Optional[float] = None


@dataclass
class BracketOrder:
    entry: Order
    take_profit: Order
    stop_loss: Order


class OMS:
    def __init__(self, broker: BrokerAdapter) -> None:
        self.broker = broker
        self.orders: Dict[str, Order] = {}

    async def place_bracket(self, bracket: BracketOrder) -> None:
        entry_id = await self.broker.place_order(vars(bracket.entry))
        self.orders[entry_id] = bracket.entry
        # In a real implementation, TP/SL orders would reference entry_id
        await self.broker.place_order(vars(bracket.take_profit))
        await self.broker.place_order(vars(bracket.stop_loss))

    async def list_open_orders(self) -> Dict[str, Order]:
        return self.orders
