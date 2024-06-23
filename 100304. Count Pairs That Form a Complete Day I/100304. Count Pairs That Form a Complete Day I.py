from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        result=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    result+=1
        return result

sln=Solution()
assert 3==sln.countCompleteDayPairs(hours = [72,48,24,3])
assert 2==sln.countCompleteDayPairs(hours = [12,12,30,24,24])
                    
                
                
        