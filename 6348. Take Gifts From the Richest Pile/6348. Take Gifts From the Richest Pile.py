from typing import List
from operator import itemgetter
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            index, element = max(enumerate(gifts), key=itemgetter(1))
            gifts[index] = math.floor(element**0.5)
        return sum(gifts)

sln=Solution()
assert 4==sln.pickGifts(gifts = [1,1,1,1], k = 4)
assert 29==sln.pickGifts(gifts = [25,64,9,4,100], k = 4)