from typing import List

class Solution: 
    
    def left(self, i, maxHeights):
        level = maxHeights[i]
        sumHeights = 0
        for j in range(i-1,-1,-1):
            level=min(level,maxHeights[j])
            sumHeights+=level
        return sumHeights
            
    def right(self, i, maxHeights):
        level = maxHeights[i]
        sumHeights = 0
        for k in range(i,len(maxHeights)):
            level=min(level,maxHeights[k])
            sumHeights+=level
        return sumHeights            
    
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        answer=0
        for i in range(len(maxHeights)):
            answer=max(answer,self.left(i,maxHeights)+self.right(i,maxHeights))
        return answer
    
sln=Solution()
assert 18==sln.maximumSumOfHeights(maxHeights = [3,2,5,5,2,3])
assert 22==sln.maximumSumOfHeights(maxHeights = [6,5,3,9,2,7])
assert 13==sln.maximumSumOfHeights(maxHeights = [5,3,4,1,1])
            
        