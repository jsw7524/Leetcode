from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        startX=ord(s[0])
        startY=ord(s[1])
        endX=ord(s[3])
        endY=ord(s[4])
        result=[]
        for i in range(startX,endX+1):
            for j in range(startY,endY+1):
                result.append(chr(i)+chr(j))
        return result
                
sln=Solution()
assert ["K1","K2","L1","L2"]==sln.cellsInRange("K1:L2")
assert ["A1","B1","C1","D1","E1","F1"]==sln.cellsInRange("A1:F1")