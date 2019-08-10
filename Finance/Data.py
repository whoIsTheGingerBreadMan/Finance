from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import datetime
import pytz

class StockData:
    def __init__(self,ticker,period_type="DAY",number_of_periods=10,frequency_type="MINUTE",number_of_frequency=5,timezone = "US/Eastern"):

        self.ticker = ticker
        self.my_share = share.Share(self.ticker)

        if period_type == "DAY":
            self.period_type = share.PERIOD_TYPE_DAY

        if frequency_type == "MINUTE":
            self.frequency_type = share.PERIOD_TYPE_DAY

        self.symbol_data = self.my_share.get_historical(self.period_type,
                                              number_of_periods,
                                              self.frequency_type,
                                              number_of_frequency)

        self.timezone = pytz.timezone(timezone)

        self.dates = [pytz.timezone('UTC').localize(pytz.datetime.datetime.fromtimestamp(time_stamp/1000)).astimezone(self.timezone) for time_stamp in
                 self.symbol_data['timestamp']]





