import os
import pandas as pd
from simulate_vpate import generate_prices, run_strategy

def test_generate_prices():
    s = generate_prices(1000, seed=1)
    assert len(s) == 1000
    assert s.min() > 0

def test_run_strategy_outputs(tmp_path):
    s = generate_prices(1000, seed=2)
    res = run_strategy(s)
    assert 'equity' in res.columns
    assert res['equity'].iloc[-1] > 0
