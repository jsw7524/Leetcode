from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        msp=0
        for i in range(n):
            for j in range(i,n):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    msp=max(nums[i] ^ nums[j], msp)
        return msp

sln=Solution()
assert 7==sln.maximumStrongPairXor(nums = [5,6,25,30])
assert 0==sln.maximumStrongPairXor(nums = [10,100])
assert 7==sln.maximumStrongPairXor(nums = [1,2,3,4,5])
                    