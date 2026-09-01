class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.days = []
        self.stack = []

        for temp in temperatures:
            self.stack.append(temp)

        if len(self.stack) == 0:
            return self.days

        if len(self.stack) == 1:
            self.days.append(0)
            return self.days

        i = 1
        while len(self.stack)!=1:
            if self.stack[i] > self.stack[0]:
                self.stack.pop(0)
                self.days.append(i-0)
            else:
                if len(self.stack)==2:
                    self.days.append(0)
                    break
                else:
                    i+=1
        
        self.days.append(0)
        return self.days

        