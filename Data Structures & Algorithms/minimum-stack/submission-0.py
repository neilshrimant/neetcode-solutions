class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = self.minStack[-1] if self.minStack and self.minStack[-1] < val else val
        self.minStack.append(self.minVal)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
