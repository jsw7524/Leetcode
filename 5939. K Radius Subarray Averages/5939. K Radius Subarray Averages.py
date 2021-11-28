from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum=[]
        tmp=0
        for i in range(len(nums)):
            tmp+=nums[i]
            prefixSum.append(tmp)
        result=[]
        for i in range(len(nums)):     
            if i - k < 0 or i+k >= len(nums):
                result.append(-1)
                continue
            result.append((prefixSum[i+k]-prefixSum[i-k] + nums[i-k] )//(2*k+1))
        return result
    
sln=Solution()
assert [-1,-1,-1,5,4,4,-1,-1,-1]==sln.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)
assert [100000]==sln.getAverages(nums = [100000], k = 0)
assert [-1]==sln.getAverages(nums = [8], k = 100000)