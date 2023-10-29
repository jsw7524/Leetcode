from typing import List

from collections import defaultdict
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        binaryNums = [reversed(bin(n)) for n in nums]
        record=defaultdict(int)
        for bn in binaryNums:
            for i, b in enumerate(bn):
                if b=='1':
                    record[i]+=1
        return sum([2**i  for i, count in record.items() if count >= k ])
    
sln=Solution()
assert 15==sln.findKOr(nums = [10,8,5,9,11,6,8], k = 1)
assert 0==sln.findKOr(nums = [2,12,1,11,4,5], k = 6)
assert 9==sln.findKOr(nums = [7,12,9,8,9,15], k = 4)
                