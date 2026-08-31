class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        dict = {')':'(',
                '}': '{',
                ']': '['
            }

        for item in s:
            if len(stk)>0 and item in [')', '}', ']'] and dict.get(item, None) == stk[0]:
                stk.pop(0)
                continue
            else:
                stk.insert(0, item)

        if len(stk) == 0:
            return True
        else: 
            return False



        