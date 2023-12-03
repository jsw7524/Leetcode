from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        tmp=[ p for p in range(1,len(mountain)-1) if mountain[p-1] < mountain[p] and mountain[p+1] < mountain[p]]
        return tmp
    
    
sln=Solution()
assert [1,3]==sln.findPeaks(mountain = [1,4,3,8,5])
assert []==sln.findPeaks(mountain = [2,4,4])
        