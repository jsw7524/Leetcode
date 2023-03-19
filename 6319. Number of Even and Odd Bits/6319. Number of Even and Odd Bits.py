from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0, 
        for i,v in enumerate((bin(n)[2:])[::-1]):
            if v == '1':
                if i%2==0:
                    even+=1
                else:
                    odd+=1
        return [even, odd]

sln=Solution()
assert [0,1]==sln.evenOddBit(n = 2)
assert [2,0]==sln.evenOddBit(n = 17)