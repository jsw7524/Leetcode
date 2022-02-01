from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        numsLen=len(nums)
        left0=[0]*(numsLen+1)
        right1=[0]*(numsLen+1)
        counter0=0
        for i in range(numsLen):
            left0[i]=counter0
            if nums[i]==0:
                counter0+=1
        left0[numsLen]=counter0
        counter1=0
        right1[numsLen]=counter1
        for i in range(numsLen-1,-1,-1):
            if nums[i]==1:
                counter1+=1            
            right1[i]=counter1            

        
        result=[]
        maxV=-1
        for i in range(numsLen+1):
            if left0[i]+right1[i] > maxV:
                maxV=left0[i]+right1[i]
                result=[]  
            if left0[i]+right1[i] == maxV:        
                result.append(i)
        return result
    
sln=Solution()

assert [0]==sln.maxScoreIndices( nums = [1,1])      
assert [3]==sln.maxScoreIndices( nums = [0,0,0])
assert [2,4]==sln.maxScoreIndices( nums = [0,0,1,0])      