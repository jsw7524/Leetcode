from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        db = sum( n for n in nums if n >= 10 )
        sg = sum( n for n in nums if n < 10 )
        return db != sg
    
sln=Solution()
assert True==sln.canAliceWin( nums = [5,5,5,25])
assert True==sln.canAliceWin(nums = [1,2,3,4,5,14])
assert False==sln.canAliceWin(nums = [1,2,3,4,10])