class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        else:
            val = min(val,self.MinStack[-1])
            self.MinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()