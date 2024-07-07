from typing import List

class Solution:
    def generate(self, s, c, n, depth):
        if n > depth:
            if c=='0':
                self.generate(s+'1','1',n,depth+1)
            elif c=='1':
                self.generate(s+'1','1',n,depth+1)                
                self.generate(s+'0','0',n,depth+1)
        else:
            self.result.add(s)
        return
                         
                
    
    def validStrings(self, n: int) -> List[str]:
        self.result=set()
        self.generate("","0",n,0)
        self.generate("","1",n,0)
        return list(self.result)
    
sln=Solution()

assert ["0","1"]==sln.validStrings(n = 1)

assert ["010","011","101","110","111"]==sln.validStrings(n = 3)
        