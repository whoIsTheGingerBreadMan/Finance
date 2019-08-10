import plotly.graph_objects as go
def CandleStick(stockData):
    return go.Figure(data =go.Candlestick(x=stockData.dates,close=stockData.close,open=stockData.open,low=stockData.low,high = stockData.high))