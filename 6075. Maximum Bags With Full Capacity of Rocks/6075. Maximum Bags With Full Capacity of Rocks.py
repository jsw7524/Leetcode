from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainedSpace=sorted([c - rocks[i] for i, c in enumerate(capacity)])
        counter=0
        for i, r in enumerate(remainedSpace):
            if additionalRocks >= r:
                additionalRocks-=r
                counter+=1
        return counter
                
sln=Solution()
assert 3==sln.maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100)          
assert 3==sln.maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2)          
