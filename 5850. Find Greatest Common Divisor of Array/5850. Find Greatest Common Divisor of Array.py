from typing import List

class Solution: 
    def GCD(self, x, y):
        if x % y ==0:
            return y
        else:
            return self.GCD(y,x%y)
    
    def findGCD(self, nums: List[int]) -> int:
        minVal=min(nums)
        maxVal=max(nums)
        return self.GCD(maxVal, minVal)
    
sln=Solution()
assert 2==sln.findGCD(nums = [2,5,6,9,10])
assert 1==sln.findGCD(nums = [7,5,6,8,3])
assert 3==sln.findGCD(nums = [3,3])
