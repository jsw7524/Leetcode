from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        result=[]
        for i, n in enumerate(nums):
            if n in primes:
                result.append(i)
        return max(result) - min(result)
    
sln=Solution()
assert 0==sln.maximumPrimeDifference(nums = [4,8,2,8])
assert 3==sln.maximumPrimeDifference(nums = [4,2,9,5,3])