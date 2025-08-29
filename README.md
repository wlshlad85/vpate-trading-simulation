# VPATE Sim Walkthrough

A minimal, self-contained Python demo inspired by ChatGPT trading discussions ("VPATE", walk-forward tests, OANDA). 
Uses synthetic prices to demonstrate a volatility-percentile adaptive trend idea. No external data or keys required.

## Quick start
```bash
python run_demo.py
```

Outputs:
- `data/sim_prices.csv`
- `data/equity_curve.csv`
- `data/equity_curve.png`

## QAA alignment
- DATAAI: data handling, basic analytics
- SEENG: modular Python, tests
- CTALG: simple adaptive rule design
- PROF: reproducible, no secrets; TRACE included

See `TRACE.md` for chat-derived provenance.
