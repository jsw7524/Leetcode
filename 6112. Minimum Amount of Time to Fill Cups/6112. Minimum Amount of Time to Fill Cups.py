from math import remainder
from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        t1=amount[0]
        amount[0]=0
        tmp=t1
        while (tmp>0):
            if amount[2] > amount[1]:
                amount[2]-=1
            else:
                amount[1]-=1
            tmp-=1  
        t2=min(amount[1], amount[2])
        remain=max(amount[1], amount[2]) - t2   
        total=t1+t2+remain
        return total
    
sln=Solution()
assert 7==sln.fillCups(amount = [5,4,4])
assert 4==sln.fillCups(amount = [1,4,2])
assert 5==sln.fillCups(amount = [5,0,0])