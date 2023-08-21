from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        argmax=max(enumerate(nums), key=lambda x: x[1])[0]
        argmin=min(enumerate(nums), key=lambda x: x[1])[0]
        return argmin + ((len(nums)-1) -argmax) if argmax > argmin else argmin + ((len(nums)-1) -argmax) -1

sln=Solution()
assert 0==sln.semiOrderedPermutation(nums = [1,3,4,2,5])
assert 3==sln.semiOrderedPermutation(nums = [2,4,1,3])
assert 2==sln.semiOrderedPermutation(nums = [2,1,4,3])