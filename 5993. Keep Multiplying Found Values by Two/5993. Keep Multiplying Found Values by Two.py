
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result = original
        while True:
            if result not in nums:
                break
            result *= 2
        return result
    
sln=Solution()

assert 1952 ==sln.findFinalValue(nums = [161,28,640,264,81,561,320,2,61,244,183,108,773,61,976,122,988,2,370,392,488,375,349,432,713,563], original = 61)
assert 8 ==sln.findFinalValue(nums = [4,7,1,16,1,2,7,13], original = 1)
assert 24 ==sln.findFinalValue(nums = [5,3,6,1,12], original = 3)
assert 4 ==sln.findFinalValue(nums = [2,7,9], original = 4)

