import abc
from typing import AsyncIterator, Dict, Any


class BrokerAdapter(abc.ABC):
    """Abstract base class for broker connectors."""

    @abc.abstractmethod
    async def connect(self) -> None:
        """Establish the underlying API connection."""
        raise NotImplementedError

    @abc.abstractmethod
    async def place_order(self, order: Dict[str, Any]) -> str:
        """Place an order and return its broker-assigned id."""
        raise NotImplementedError

    @abc.abstractmethod
    async def stream_quotes(self, symbol: str) -> AsyncIterator[Dict[str, Any]]:
        """Yield quote events for *symbol* as dictionaries."""
        yield {}
