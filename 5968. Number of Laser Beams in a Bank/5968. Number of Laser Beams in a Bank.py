from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sumRow = list(map(lambda g: sum( [1 if k == '1' else 0 for k in g] ),bank))
        sumRow= list(filter(lambda x: x>0, sumRow))
        result=0
        for i in range(len(sumRow)-1):
            result+=sumRow[i]*sumRow[i+1]
        return result
    
sln=Solution()
assert 8==sln.numberOfBeams(bank = ["011001","000000","010100","001000"])
assert 0==sln.numberOfBeams(bank = ["000","111","000"])
