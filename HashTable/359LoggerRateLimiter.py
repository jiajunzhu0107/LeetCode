# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = timestamp + 10
            return True
        else:
            if timestamp < self.dict[message]:
                return False
            else:
                self.dict[message] = timestamp + 10
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)