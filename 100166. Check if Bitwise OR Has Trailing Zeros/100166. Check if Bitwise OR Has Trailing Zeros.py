from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return True if len([n for n in nums if n%2==0]) > 1 else False
    
sln=Solution()
assert False==sln.hasTrailingZeros(nums = [1,3,5,7,9])
assert True==sln.hasTrailingZeros(nums = [2,4,8,16])
assert True==sln.hasTrailingZeros(nums = [1,2,3,4,5])
        