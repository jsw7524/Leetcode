from typing import Counter


class Solution:
    def countEven(self, num: int) -> int:
        counter=0
        for i in range(2,num+1):
            dSum=0
            for d in str(i):
                dSum+=int(d)
            if dSum%2==0:
                counter+=1
        return counter

sln=Solution()
assert 14==sln.countEven(num = 30)                
assert 2==sln.countEven(num = 4)
                
