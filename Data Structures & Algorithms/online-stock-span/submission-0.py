class StockSpanner:

    def __init__(self):
        self.stock_price = []

    def next(self, price: int) -> int:
        result = 1
        while self.stock_price and self.stock_price[-1][0] <= price:
            result += self.stock_price[-1][1]
            self.stock_price.pop()
        self.stock_price.append((price, result))
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)