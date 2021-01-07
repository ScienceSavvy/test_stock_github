import numpy as np


class Company:

    #This var stores the bought/sold stock transactions for this company
    stockList = []

    # Add underscore before ticker, etc to prevent recursion error
    def __init__(self, ticker, date, close_price, volume):
        self._ticker = ticker
        self._date = date
        self._close_price = close_price
        self._volume = volume

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, new_ticker):
        self._ticker = new_ticker

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @property
    def close_price(self):
        return self._close_price

    @close_price.setter
    def close_price(self, new_close_price):
        self._close_price = new_close_price

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    # Returns the specified moving average of this company
    def movingavg(self, window):
        weights = np.repeat(1.0, window) / window
        smas = np.convolve(self.close_price, weights, "valid")
        smasList = smas.tolist()
        # Pads list with zeros to account for invalid sma at beginning
        for index in range(0, window - 1):
            smasList.insert(0, 0)
        return smasList
