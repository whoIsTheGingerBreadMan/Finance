import numpy as np


def simple_moving_average(data, window=10):
    sma = np.cumsum(data)
    sma = sma[window:] - sma[:-window]
    return sma / window


def relative_strength_index(returns, window=14):
    all_returns_in_window = returns[:window]
    positive_returns_in_window = all_returns_in_window[all_returns_in_window > 0]
    negative_returns_in_window = all_returns_in_window[all_returns_in_window < 0]
    negative_returns_mean = np.mean(negative_returns_in_window) * -1
    positive_returns_mean = np.mean(positive_returns_in_window)
    initial_rsi = 100 - (100 / (1 + (positive_returns_mean / negative_returns_mean)))
    rsi = [initial_rsi]
    for r in returns[window:]:
        if r < 0:
            negative_returns_mean = (negative_returns_mean * (window - 1) - r) / window
        else:
            positive_returns_mean = (positive_returns_mean * (window - 1) + r) / window
        next_rsi = 100 - (100 / (1 + (positive_returns_mean / negative_returns_mean)))
        rsi.append(next_rsi)
    return rsi
