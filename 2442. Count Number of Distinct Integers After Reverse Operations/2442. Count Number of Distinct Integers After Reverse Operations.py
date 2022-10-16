from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result=set()
        for n in nums:
            #tmp=int(str(n)[::-1])
            result.add(int((str(n))[::-1]))
        for n in nums:
            result.add(n)
        return len(result)

sln=Solution()
assert 5==sln.countDistinctIntegers(nums = [1,2,3,4,100])
assert 1==sln.countDistinctIntegers(nums = [2,2,2])
assert 6==sln.countDistinctIntegers(nums = [1,13,10,12,31])
        