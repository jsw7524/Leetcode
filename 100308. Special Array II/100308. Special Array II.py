from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        preSum=[0]
        tmp=0
        for i in range(1,len(nums)):
            tmp+=(nums[i]+nums[i-1])%2
            preSum.append(tmp)
        answers=[]
        for start, end in queries:
            if end-start==0:
                answers.append(True)
            elif preSum[end] - preSum[start] == end -start:
                answers.append(True)
            else:
                answers.append(False)
        return answers

sln=Solution()
assert [True,True,True,True,True,True,True,True]==sln.isArraySpecial([1],[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])  
assert [False,True]==sln.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]])  
assert [False]==sln.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]])  
        