import bisect
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        info = { i:0 for i in range(24) }
        for h in hours:
            info[h%24]+=1
        result=0
        for i in range(1,12):
            result+=(info[i]*info[24-i])
        return result+(info[0]*(info[0]-1)//2)+(info[12]*(info[12]-1)//2)
    
sln=Solution()
assert 3==sln.countCompleteDayPairs(hours = [72,48,24,3])
assert 3==sln.countCompleteDayPairs(hours = [72,48,24,3])
assert 2==sln.countCompleteDayPairs(hours = [12,12,30,24,24])
                    
      