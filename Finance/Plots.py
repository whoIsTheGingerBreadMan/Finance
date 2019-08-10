import plotly.graph_objects as go


def CandleStick(stockData):
    candle_stick = go.Candlestick(
        x=stockData.dates, close=stockData.close, open=stockData.open, low=stockData.low, high=stockData.high
    )
    output_figure = go.Figure(data=candle_stick)
    return output_figure
