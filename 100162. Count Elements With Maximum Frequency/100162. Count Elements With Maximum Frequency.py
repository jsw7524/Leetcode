from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter=Counter(nums)
        return sum([f for f in counter.values() if f == max(counter.values())])
    
sln=Solution()
assert 5==sln.maxFrequencyElements(nums = [1,2,3,4,5])
assert 4==sln.maxFrequencyElements(nums = [1,2,2,3,1,4])