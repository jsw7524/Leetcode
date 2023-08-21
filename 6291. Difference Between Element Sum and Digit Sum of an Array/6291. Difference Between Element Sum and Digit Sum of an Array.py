from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum=0
        for n in nums:
            for d in str(n):
                digitSum+=ord(d)-ord('0')
        return abs(sum(nums)-digitSum)
    
sln=Solution()
assert 0==sln.differenceOfSum(nums = [1,2,3,4])
assert 9==sln.differenceOfSum(nums = [1,15,6,3])
                