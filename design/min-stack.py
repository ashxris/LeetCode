class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, value: int) -> None:
        self.s.insert(0,value)
        self.mins.insert(0, min(value, self.min[0]))

    def pop(self) -> None:
        self.s.pop(0)

    def top(self) -> int:
        return self.s[0]

    def getMin(self) -> int:
        return self.mins[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()