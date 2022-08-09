from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter=0
        n=len(nums)
        record=[0]*400
        for i in range(n):
            record[nums[i]]=1
        for i in range(n):
            if record[nums[i] + diff]==1 and record[nums[i] + 2*diff]==1:
                counter+=1
        return counter

sln=Solution()
assert 2==sln.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2)
assert 2==sln.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)
            
            