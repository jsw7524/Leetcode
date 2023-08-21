import bisect
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        prefixSum=[]
        nums.sort()
        tmp=0
        for n in nums:
            tmp+=n
            prefixSum.append(tmp)
        numsLen=len(nums)
        result=[]
        for q in queries:
            i=bisect.bisect_right(nums,q)
            if i==numsLen:
                ans=numsLen*q-prefixSum[-1]
            elif i==0:
                ans=prefixSum[-1]-numsLen*q
            else:
                ans= (q*i - (prefixSum[i]-nums[i])) + ((prefixSum[-1]-prefixSum[i]+nums[i]) - q*(numsLen-i))
            result.append(ans)
        return result

sln=Solution()
assert [20]==sln.minOperations(nums = [2,9,6,3], queries = [10])   
assert [14,10]==sln.minOperations(nums = [3,1,6,8], queries = [1,5])         