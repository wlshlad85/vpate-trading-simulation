# VPATE Trading Simulation Project

## 📊 Project Overview

This project implements a **Volatility-Percentile Adaptive Trend Entry (VPATE)** trading strategy simulation in Python. The system demonstrates an adaptive trading approach that adjusts its parameters based on market volatility conditions, using synthetic price data for testing and validation.

### Key Features
- **Adaptive Strategy**: Dynamically adjusts lookback periods based on volatility percentiles
- **Synthetic Data Generation**: Creates realistic market price movements with regime shifts
- **Backtesting Engine**: Complete simulation framework with performance metrics
- **Visualization**: Automated equity curve generation and analysis
- **Test Suite**: Comprehensive unit tests for strategy validation

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/wlshlad85/vpate-trading-simulation.git
cd vpate-trading-simulation
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the demo**
```bash
python run_demo.py
```

### Expected Output
The simulation will generate:
- `data/sim_prices.csv` - Synthetic price data used for testing
- `data/equity_curve.csv` - Strategy performance over time
- `data/equity_curve.png` - Visual representation of equity growth
- Console output showing CAGR (Compound Annual Growth Rate) proxy

## 📁 Project Structure

```
vpate-trading-simulation/
│
├── simulate_vpate.py      # Core strategy implementation
├── run_demo.py            # Main execution script
├── requirements.txt       # Project dependencies
│
├── data/                  # Output directory
│   ├── sim_prices.csv     # Generated price data
│   ├── equity_curve.csv   # Strategy returns
│   └── equity_curve.png   # Performance visualization
│
├── tests/                 # Test suite
│   └── test_strategy.py   # Unit tests for strategy components
│
└── docs/
    ├── README.md          # This file
    └── TRACE.md          # Development history and provenance
```

## 🔬 Technical Details

### Strategy Components

#### 1. **Price Generation** (`generate_prices()`)
- Generates synthetic market data using geometric random walk
- Incorporates regime shifts and volatility spikes
- Produces realistic price patterns for testing

#### 2. **Volatility Analysis** (`rolling_volatility()`)
- Calculates rolling standard deviation of returns
- Default window: 20 periods
- Used to assess market conditions

#### 3. **Percentile Ranking** (`percentile_rank()`)
- Determines volatility percentile over 252-period window
- Classifies market regimes (low/medium/high volatility)
- Triggers adaptive parameter adjustments

#### 4. **Donchian Breakout** (`donchian_breakout()`)
- Implements channel breakout logic
- Long entry: Price exceeds N-period high
- Exit: Price falls below N-period low
- Lookback period varies based on volatility

#### 5. **VPATE Signal Generation** (`vpate_signal()`)
- **Adaptive lookback periods**:
  - Low volatility (< 30th percentile): 30 periods
  - Normal volatility: 50 periods (base)
  - High volatility (> 70th percentile): 80 periods
- Combines volatility assessment with trend following
- Generates binary position signals (0 or 1)

### Performance Metrics

The strategy calculates:
- **Equity Curve**: Cumulative returns over time
- **CAGR Proxy**: Annualized return estimate
- **Risk-Adjusted Returns**: Through adaptive volatility management

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/test_strategy.py -v
```

Tests verify:
- Price generation consistency
- Signal generation logic
- Strategy execution
- Edge case handling

## 📈 Strategy Philosophy

The VPATE strategy operates on the principle that market behavior varies with volatility regimes:

1. **Low Volatility Environments**: Markets tend to trend smoothly, so we use shorter lookback periods (30) for quicker trend detection
2. **High Volatility Environments**: Markets are more erratic, requiring longer lookback periods (80) to filter noise
3. **Adaptive Approach**: By dynamically adjusting parameters, the strategy aims to capture trends while managing risk

## 🎓 Academic Context

### QAA Alignment
- **DATAAI**: Demonstrates data handling and basic analytics
- **SEENG**: Showcases modular Python design and testing practices
- **CTALG**: Implements adaptive algorithmic trading rules
- **PROF**: Ensures reproducibility with fixed seeds and documented methodology

### Learning Objectives
- Understanding of algorithmic trading concepts
- Implementation of adaptive strategies
- Backtesting methodology
- Risk management through volatility assessment
- Software engineering best practices in finance

## 📊 Sample Results

When you run the demo, you'll see:
- Generated synthetic prices with realistic market dynamics
- Strategy position changes based on volatility conditions
- Equity curve showing cumulative performance
- CAGR calculation for performance assessment

## 🔄 Extending the Project

Potential enhancements:
1. **Real Market Data**: Replace synthetic data with historical prices
2. **Additional Indicators**: Incorporate momentum, volume, or sentiment
3. **Risk Management**: Add position sizing and stop-loss logic
4. **Multi-Asset**: Extend to portfolio-level strategies
5. **Machine Learning**: Use ML for parameter optimization
6. **Live Trading**: Connect to broker APIs (e.g., OANDA, mentioned in TRACE)

## 📝 Documentation

- **README.md**: This comprehensive guide
- **TRACE.md**: Development history and ChatGPT discussion origins
- **Code Comments**: Inline documentation throughout source files

## 🤝 Contributing

This is an academic project. For questions or suggestions:
1. Open an issue on GitHub
2. Contact through academic channels
3. Fork and submit pull requests for improvements

## 📜 License

Academic use - please cite if using for research or coursework.

## 🙏 Acknowledgments

- Inspired by ChatGPT trading strategy discussions
- Developed for academic demonstration purposes
- Uses volatility-percentile concepts from quantitative finance literature

## ⚠️ Disclaimer

This is an educational simulation using synthetic data. It is not intended for real trading. Always conduct thorough research and consider risks before any actual trading activities.

---

**Author**: [Your Name]  
**Course**: [Course Name/Number]  
**Institution**: [Your University]  
**Date**: August 2025  
**Repository**: https://github.com/wlshlad85/vpate-trading-simulation
