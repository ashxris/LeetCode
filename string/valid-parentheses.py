class Solution:
    def isValid(self, s: str) -> bool:
        self.stk = []

        dict = {
            '(':')',
            '{': '}',
            '[': ']'
        }

        for item in s:
                if (len(stk)>0 and s[item] in list(dict.values) and dict.get(stk[0], None) == s[item]):
                    stk.pop()
                    continue
                else:
                    stk.insert(0, s[item])

        if len(stk) == 0:
                return True
            else: 
                return False



        