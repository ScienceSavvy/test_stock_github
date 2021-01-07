class Stock:
    priceDiff = 0;
    saleClosed = False
    isWin = False;

    def __init__(self, ticker, buyDate, sellDate, bidPrice, askPrice):
        self._ticker = ticker
        self._buyDate = buyDate
        self._sellDate = sellDate
        self._bidPrice = bidPrice
        self._askPrice = askPrice

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, new_ticker):
        self._ticker = new_ticker

    @property
    def buyDate(self):
        return self._buyDate

    @buyDate.setter
    def buyDate(self, new_buyDate):
        self._buyDate = new_buyDate

    @property
    def sellDate(self):
        return self._sellDate

    @sellDate.setter
    def sellDate(self, new_sellDate):
        self._sellDate = new_sellDate

    @property
    def bidPrice(self):
        return self._bidPrice

    @bidPrice.setter
    def ticker(self, new_bidPrice):
        self._bidPrice = new_bidPrice

    @property
    def askPricer(self):
        return self._askPrice

    @askPricer.setter
    def askPrice(self, new_askPrice):
        self._askPrice = new_askPrice

    def getPriceDiff(self):
        priceDiff = self._bidPrice - self._askPrice
        return priceDiff

    def isProfit(self):
        if self.priceDiff < 0:
            return True
        else:
            return False

    # Execute this function when the stock is sold
    def closeSale(self, sellDate, sellPrice):
        self.saleClosed = True
        self._sellDate = sellDate
        self._bidPrice = sellPrice
        self.priceDiff = self._bidPrice - self._askPrice
        if self.priceDiff > 0:
            self.isWin = True
