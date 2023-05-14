from typing import List

class Solution:
    
    def check(self, value):
        pos = 0
        curValue=value
        #ori=[curValue]
        while pos < self.n - 1:
            if self.derived[pos]==1:
                curValue= 1 if curValue == 0 else 0
            else: 
                curValue= 1 if curValue == 1 else 0
            #ori.append(curValue)               
            pos+=1
        if curValue == value and self.derived[pos]==0:
            return True         
        elif curValue != value and self.derived[pos]==1:
            return True
        return False            

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        self.n=len(derived)
        self.derived=derived
        a=self.check(0)
        b=self.check(1)
        return  a or b
        
sln=Solution()
assert False==sln.doesValidArrayExist(derived = [1,0])
assert True==sln.doesValidArrayExist(derived = [1,1])
assert True==sln.doesValidArrayExist(derived = [1,1,0])