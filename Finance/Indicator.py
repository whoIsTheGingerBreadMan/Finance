import numpy as np


def simple_moving_average(data, window=10):
    sma = np.cumsum(data)
    sma = sma[window:] - sma[:-window]
    return sma / window


def relative_strength_index(stockData):
    return
