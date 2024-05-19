from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length=len(nums)
        if 1==length:
            return True
        for i in range(1,length):
            if (nums[i]+nums[i-1])%2==0:
                return False
        return True

sln=Solution()
assert False==sln.isArraySpecial(nums = [4,3,1,6])
assert True==sln.isArraySpecial(nums = [2,1,4])
assert True==sln.isArraySpecial(nums = [1])
            
        