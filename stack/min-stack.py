class MinStack:

    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        if type(value) == int:
            self.s.insert(0,value)

    def pop(self) -> None:
        if len(self.s)==0:
            raise Exception("Stack is empty.")
        else:
            self.s.pop(0)

    def top(self) -> int:
        if len(self.s)==0:
            raise Exception("Stack is empty.")
        else :
            return self.s[0]

    def getMin(self) -> int:
        return min(self.s)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()