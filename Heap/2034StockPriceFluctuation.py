class StockPrice:

    def __init__(self):
        self.stockPrice = {}
        self.maxPriceHeap = []
        self.minPriceHeap = []
        self.currentTime = -inf
        

    def update(self, timestamp: int, price: int) -> None:
        
        self.stockPrice.update({timestamp:price})
        heappush(self.maxPriceHeap, (-1 * price, timestamp))
        heappush(self.minPriceHeap, (price, timestamp))
        

        self.currentTime = max(self.currentTime,timestamp)

    def current(self) -> int:
        return self.stockPrice[self.currentTime]
        

    def maximum(self) -> int:
        # print(self.maxPriceHeap)
        while self.maxPriceHeap:
            price, time = self.maxPriceHeap[0]
            if self.stockPrice[time] == -1 * price:
                return -1* price
            else:
                heappop(self.maxPriceHeap)
        

    def minimum(self) -> int:
        while self.minPriceHeap:
            price, time = self.minPriceHeap[0]
            if self.stockPrice[time] == price:
                return price
            else:
                heappop(self.minPriceHeap)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()