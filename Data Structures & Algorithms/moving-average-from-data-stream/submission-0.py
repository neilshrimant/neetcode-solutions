class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []
        self.l = 0
        self.r = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.nums.append(val)
        self.r += 1
        curr_size = self.r - self.l
        if curr_size > self.size:
            self.sum -= self.nums[self.l]
            curr_size -= 1
            self.l += 1
        return self.sum / curr_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
