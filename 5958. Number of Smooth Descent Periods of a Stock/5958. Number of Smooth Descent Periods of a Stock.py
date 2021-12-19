from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        period=[prices[0]]
        answer=0
        for p in prices[1:]:
            if period[-1]-1!=p:
                lenP=len(period)
                answer+=((lenP+1)*lenP)//2
                period.clear()
            period.append(p)
        lenP=len(period)
        answer+=((lenP+1)*lenP)//2
        return answer

sln=Solution()
    
assert 4==sln.getDescentPeriods(prices = [8,6,7,7])            
assert 1==sln.getDescentPeriods(prices = [1])     
assert 7==sln.getDescentPeriods(prices = [3,2,1,4])   