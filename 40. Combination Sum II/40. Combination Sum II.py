from typing import List

class Solution:
    
    def DFS(self, i, value):
        if value > self.target or i >= self.n:
            return   
        if self.target == value:
            self.result.append(self.tmp.copy())
        else:
            prev=0
            for k in range(i+1,self.n):
                if prev==self.candidates[k]:
                    continue
                self.tmp.append(self.candidates[k])
                self.DFS(k,value+self.candidates[k])
                prev=self.tmp.pop()
        return
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n=len(candidates)
        self.target=target
        self.tmp=[]
        self.result=[]
        self.candidates=sorted(candidates)
        self.DFS(-1,0)
        return self.result
        
        
sln=Solution()
assert [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]==sln.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)


assert [
[1,2,2],
[5]
]==sln.combinationSum2(candidates = [2,5,2,1,2], target = 5)
                    
                
            