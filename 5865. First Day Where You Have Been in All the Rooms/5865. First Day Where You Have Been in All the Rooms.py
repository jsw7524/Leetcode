from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        i=0
        dp=[0]*n
        days=0
        #print(days,i)
        while i < n-1:
            dp[i]+=1
            if dp[i]%2==1:
                i=nextVisit[i]
            else:
                i=(i+1)%n
            days+=1
            #print(days,i)
        return days
    
sln=Solution()
assert 2==sln.firstDayBeenInAllRooms(nextVisit = [0,0])
assert 6==sln.firstDayBeenInAllRooms(nextVisit = [0,0,2])
assert 6==sln.firstDayBeenInAllRooms(nextVisit = [0,1,2,0])