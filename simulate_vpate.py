import numpy as np
import pandas as pd

def generate_prices(n=3000, seed=42):
    rng = np.random.default_rng(seed)
    # geometric random walk with regime shifts
    steps = rng.normal(0, 0.01, size=n)
    # occasional volatility spikes
    spikes = rng.choice([0,1], size=n, p=[0.98,0.02]) * rng.normal(0,0.05,size=n)
    r = steps + spikes
    price = 100 * np.exp(np.cumsum(r))
    return pd.Series(price, name='close')

def rolling_volatility(series, window=20):
    return series.pct_change().rolling(window).std()

def percentile_rank(a, window=252):
    s = pd.Series(a)
    # rolling percentile rank of last value within window
    def prk(x):
        last = x.iloc[-1]
        return (x.rank(pct=True).iloc[-1])
    return s.rolling(window).apply(prk, raw=False)

def donchian_breakout(series, lookback):
    high = series.rolling(lookback).max().shift(1)
    low = series.rolling(lookback).min().shift(1)
    long = series > high
    flat = series < low
    pos = pd.Series(0, index=series.index, dtype=float)
    pos[long] = 1.0
    pos[flat] = 0.0
    pos = pos.ffill().fillna(0.0)
    return pos

def vpate_signal(close, base_lb=50, low_vol_lb=30, high_vol_lb=80):
    vol = rolling_volatility(close, 20)
    vpr = percentile_rank(vol.fillna(method='bfill'), 252).fillna(0.5)
    # adapt lookback: shorter in low vol, longer in high vol
    lb = pd.Series(base_lb, index=close.index, dtype=float)
    lb[vpr < 0.3] = low_vol_lb
    lb[vpr > 0.7] = high_vol_lb
    # compute position via donchian per-step using varying lookback
    pos = pd.Series(0.0, index=close.index)
    for i in range(len(close)):
        L = int(max(10, min(200, lb.iloc[i])))
        if i < L+1:
            pos.iloc[i] = 0.0
        else:
            hi = close.iloc[i-L:i].max()
            lo = close.iloc[i-L:i].min()
            if close.iloc[i] > hi: pos.iloc[i] = 1.0
            elif close.iloc[i] < lo: pos.iloc[i] = 0.0
            else: pos.iloc[i] = pos.iloc[i-1]
    return pos, vpr

def run_strategy(close, cost_bp=1.0):
    pos, vpr = vpate_signal(close)
    ret = close.pct_change().fillna(0.0)
    pos_shift = pos.shift(1).fillna(0.0)
    gross = pos_shift * ret
    trades = pos_shift.diff().abs().fillna(0.0)
    cost = trades * (cost_bp/10000.0)
    net = gross - cost
    eq = (1+net).cumprod()
    df = pd.DataFrame({'close':close, 'pos':pos, 'vpr':vpr, 'ret':ret, 'net':net, 'equity':eq})
    return df
