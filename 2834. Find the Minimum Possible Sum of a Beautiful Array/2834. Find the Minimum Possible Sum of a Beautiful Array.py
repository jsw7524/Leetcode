import math

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        result=[]
        for i in range(1, (target//2)+1):
            result.append(i)
        tmp=target
        while len(result) < n:
            result.append(tmp)
            tmp+=1
        return sum(result)
    
sln=Solution()
assert 1==sln.minimumPossibleSum(n = 1, target = 1)    
assert 8==sln.minimumPossibleSum(n = 3, target = 3)      
assert 4==sln.minimumPossibleSum(n = 2, target = 3)
            
        
        
        
            
            