from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        record=[0] *101
        for n in  nums:
            record[n]=1
        return sum(record[1:])
    
sln=Solution()
assert 0==sln.minimumOperations(nums = [0])
assert 3==sln.minimumOperations(nums = [1,5,0,3,5])       