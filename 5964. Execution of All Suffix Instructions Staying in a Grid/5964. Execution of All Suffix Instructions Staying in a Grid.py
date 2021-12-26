from typing import List

class Solution:
    def execute(self, n, y, x, instruction):
        if instruction == 'U':
            y-=1
        if instruction == 'D':
            y+=1       
        if instruction == 'L':
            x-=1
        if instruction == 'R':
            x+=1
        if 0 <= y < n and 0 <= x < n:
            return (True, y, x)
        return (False,99999,99999)
                     
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []  
        for k in range(len(s)):  
            y=startPos[0]
            x=startPos[1]
            steps=0
            for i in s[k:]:
                isOk, y, x=self.execute(n, y, x, i)
                if isOk == False:
                    break                    
                else:
                    steps+=1
            result.append(steps)     
        return result

sln=Solution()
assert [1,5,4,3,1,0]==sln.executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU")
assert [4,1,0,0]==sln.executeInstructions(n = 2, startPos = [1,1], s = "LURD")                      
assert [0,0,0,0]==sln.executeInstructions(n = 1, startPos = [0,0], s = "LRUD")                