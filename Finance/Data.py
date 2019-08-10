from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import datetime
import pytz
from .Plots import CandleStick
from .Indicator import simple_moving_average


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

        self.close = self.symbol_data["close"]
        self.open = self.symbol_data["open"]
        self.high = self.symbol_data["high"]
        self.low = self.symbol_data["low"]
        self.volume = self.symbol_data["volume"]

    def plot_candle_stick(self):
        plot = CandleStick(self)
        plot.show()

    def moving_average(self, window=10, based_on="close"):
        if based_on == "close":
            data = self.close
        elif based_on == "open":
            data = self.open
        else:
            print("The data doesn't exist")
            return

        return simple_moving_average(data, window)
