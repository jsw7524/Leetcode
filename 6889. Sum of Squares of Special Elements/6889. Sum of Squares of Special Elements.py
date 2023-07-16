from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        answer=0
        for i in range(1, n+1):
            if n % i == 0:
                answer+=nums[i-1]**2
        return answer

sln=Solution()
assert 63==sln.sumOfSquares(nums = [2,7,1,19,18,3])
assert 21==sln.sumOfSquares(nums = [1,2,3,4])
                
                
        