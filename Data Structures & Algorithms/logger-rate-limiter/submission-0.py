class Logger:

    def __init__(self):
        self.check_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.check_map:
            self.check_map[message] = timestamp
            return True
        if timestamp - self.check_map[message] >= 10:
            self.check_map[message] = timestamp
            return True
        else:
            return False
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
