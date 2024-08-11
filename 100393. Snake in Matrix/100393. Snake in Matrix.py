from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y= 0, 0
        for c in commands:
            if c=="RIGHT":
                x+=1
            elif c=="LEFT":
                x-=1
            elif c=="UP":
                y-=1
            elif c=="DOWN":
                y+=1
        return y*n+x
    
sln=Solution()
assert 3==sln.finalPositionOfSnake(n = 2, commands = ["RIGHT","DOWN"])
assert 1==sln.finalPositionOfSnake(n = 3, commands = ["DOWN","RIGHT","UP"])


        