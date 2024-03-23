class TradeEntry:
    def __init__(self, politician, party, issuer, ticker, published, traded, filed_after, buy_or_sell, owner, size, price):
        self.Politician = politician
        self.Party = party
        self.Issuer = issuer
        self.Ticker = ticker
        self.Published = published
        self.Traded = traded
        self.FiledAfter = filed_after
        self.BuyOrSell = buy_or_sell
        self.Owner = owner
        self.Size = size
        self.Price = price

    def __str__(self):
        return f"Politician: {self.Politician}, Party: {self.Party}, Issuer: {self.Issuer}, Ticker: {self.Ticker}, " \
               f"Published: {self.Published}, Traded: {self.Traded}, FiledAfter: {self.FiledAfter}, BuyOrSell: {self.BuyOrSell}, " \
               f"Owner: {self.Owner}, Size: {self.Size}, Price: {self.Price}"
    
    def format(self):
        """Format the trade entry as a list of values."""
        return [getattr(self, field) for field in ['Politician', 'Party', 'Issuer', 'Ticker', 'Published', 'Traded',
                                                   'FiledAfter', 'BuyOrSell', 'Owner', 'Size', 'Price']]
