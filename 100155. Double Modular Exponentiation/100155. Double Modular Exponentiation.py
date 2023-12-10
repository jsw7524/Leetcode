from typing import List

class Solution:
    
    def modular(self, b, p, m):
        ans=1
        for i in range(p):
            ans=(ans*b)%m
        return ans
    
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans=[]
        for i, (a, b, c, m) in enumerate(variables):
            tmp=self.modular(a,b,10)
            result=self.modular(tmp,c,m)
            if result==target:
                ans.append(i)
        return ans
    
sln=Solution()
assert []==sln.getGoodIndices(variables = [[39,3,1000,1000]], target = 17)
assert [0,2]==sln.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2)
                
            
        