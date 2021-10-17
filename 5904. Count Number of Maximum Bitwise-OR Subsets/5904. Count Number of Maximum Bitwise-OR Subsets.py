from typing import List
from itertools import chain, combinations

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        MaximumBitwiseOR=0
        for n in nums:
            MaximumBitwiseOR|=n
        allSubset = chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))
        result=0
        for subset in allSubset:
            tmp=0
            for e in subset:
                tmp|=e
            if tmp == MaximumBitwiseOR:
                result+=1
        return result
                
    
sln=Solution()
assert 2==sln.countMaxOrSubsets(nums = [3,1])
assert 6==sln.countMaxOrSubsets(nums = [3,2,1,5])
assert 7==sln.countMaxOrSubsets(nums = [2,2,2])
                