from typing import List
from random import randrange
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        totalSum=(n+m)*mean
        result=[]
        rsum=sum(rolls)
        if (n>(totalSum-rsum) or rsum > totalSum or totalSum > rsum+6*n):
            return result
        remainder=totalSum-rsum
        ragv=remainder//n
        i=0
        while i < n:
            result.append(ragv)
            remainder-=ragv
            i+=1
            
        while remainder > 0:
            tmp=randrange(n)
            if result[tmp]<6:
                result[tmp]+=1
                remainder-=1
        return result 
        

sln=Solution()
# assert [6,6]==sln.missingRolls(rolls = [3,2,4,3], mean = 4, n = 2)
# assert []==sln.missingRolls(rolls = [1,2,3,4], mean = 6, n = 4)
# assert [2,2,2,3]==sln.missingRolls(rolls = [1,5,6], mean = 3, n = 4)
# assert []==sln.missingRolls(rolls = [6,3,4,3,5,3], mean = 1, n = 6)


assert []==sln.missingRolls(rolls = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], mean = 2, n = 53)

