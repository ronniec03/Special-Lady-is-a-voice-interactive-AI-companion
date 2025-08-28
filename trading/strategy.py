"""Example strategy that submits a single bracket order when started."""
from __future__ import annotations

from .oms import Order, BracketOrder, OMS


class ExampleStrategy:
    def __init__(self, oms: OMS) -> None:
        self.oms = oms

    async def run(self) -> None:
        entry = Order(symbol="AAPL", side="buy", qty=1)
        tp = Order(symbol="AAPL", side="sell", qty=1, limit=9999)
        sl = Order(symbol="AAPL", side="sell", qty=1, stop=0)
        bracket = BracketOrder(entry=entry, take_profit=tp, stop_loss=sl)
        await self.oms.place_bracket(bracket)
