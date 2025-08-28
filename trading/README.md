# Trading Skeleton

This directory contains a minimal event-driven trading stack for experimentation.

Features:
- Async adapters for Interactive Brokers and Coinbase Advanced Trade (skeletons).
- In-memory order management system with bracket order support.
- Example strategy submitting a single bracket order.
- Prometheus metrics endpoint.

## Usage
```bash
python -m trading.main
```

All adapters are placeholders and need proper API integration before live use.
