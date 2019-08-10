from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import datetime
import numpy as np
import pytz
from .Plots import CandleStick, LinePlot
from .Indicator import simple_moving_average, relative_strength_index


class StockData:
    def __init__(
        self,
        ticker,
        period_type="DAY",
        number_of_periods=10,
        frequency_type="MINUTE",
        number_of_frequency=5,
        timezone="US/Eastern",
    ):

        self.ticker = ticker
        self.my_share = share.Share(self.ticker)

        if period_type == "DAY":
            self.period_type = share.PERIOD_TYPE_DAY

        if frequency_type == "MINUTE":
            self.frequency_type = share.FREQUENCY_TYPE_MINUTE

        self.symbol_data = self.my_share.get_historical(
            self.period_type, number_of_periods, self.frequency_type, number_of_frequency
        )

        self.timezone = pytz.timezone(timezone)

        self.dates = [
            pytz.timezone("UTC")
            .localize(pytz.datetime.datetime.fromtimestamp(time_stamp / 1000))
            .astimezone(self.timezone)
            for time_stamp in self.symbol_data["timestamp"]
        ]

        self.close = np.array(self.symbol_data["close"])
        self.open = np.array(self.symbol_data["open"])
        self.high = np.array(self.symbol_data["high"])
        self.low = np.array(self.symbol_data["low"])
        self.volume = np.array(self.symbol_data["volume"])
        self.returns = self.close - self.open
        self.calculated_indicators = {}

    def RSI(self, window=14):

        new_indicator = relative_strength_index(self.returns / self.open, window=window)
        self.add_indicator("RSI" + str(window), {"properties": {"window": window}, "value": new_indicator})

    def add_indicator(self, name, value):
        self.calculated_indicators[name] = value

    def plot_candle_stick(self):
        plot = CandleStick(self)
        plot.show()

    def plot_line(self, field="close"):
        plot = LinePlot(self, field)
        plot.show()

    def moving_average(self, window=10, field="close"):
        data = self.__dict__[field]
        sma = simple_moving_average(data, window)
        return sma
