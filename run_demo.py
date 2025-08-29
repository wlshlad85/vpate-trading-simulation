import pandas as pd
import matplotlib.pyplot as plt
from simulate_vpate import generate_prices, run_strategy

def main():
    close = generate_prices(n=4000, seed=7)
    res = run_strategy(close)
    # Save data
    res[['close']].to_csv('data/sim_prices.csv')
    res[['equity']].to_csv('data/equity_curve.csv')
    # Plot equity curve
    plt.figure()
    res['equity'].plot()
    plt.title('VPATE Simulated Equity Curve')
    plt.xlabel('Index')
    plt.ylabel('Equity')
    plt.tight_layout()
    plt.savefig('data/equity_curve.png', dpi=150)
    # Also show a brief print
    print('CAGR proxy:', (res['equity'].iloc[-1])**(252/len(res)) - 1)

if __name__ == '__main__':
    main()
