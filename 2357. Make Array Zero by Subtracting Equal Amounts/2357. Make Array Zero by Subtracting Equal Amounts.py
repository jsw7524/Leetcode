

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        record=[0] *101
        for n in  nums:
            record[n]=1
        return sum(record[1:])
    