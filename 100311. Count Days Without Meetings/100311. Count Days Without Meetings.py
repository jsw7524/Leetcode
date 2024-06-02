from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        schedule=[]
        meetings.sort()
        previousStart=meetings[0][0]
        previousEnd=meetings[0][1]
        schedule.append([previousStart,previousEnd])
        for m in meetings[1:]:
            currentStart=m[0]
            currentEnd=m[1]
            if currentStart > previousEnd:
                schedule.append([currentStart,currentEnd])                
                previousStart=currentStart
                previousEnd=currentEnd
            else:
                if currentEnd > previousEnd:
                    schedule[-1][1]=currentEnd
                    previousEnd=currentEnd
        for s in schedule:
            days-=(s[1]-s[0]+1)
        return days

sln=Solution()
assert 0==sln.countDays(days = 6, meetings = [[1,6]])
assert 1==sln.countDays(days = 5, meetings = [[2,4],[1,3]])
assert 2==sln.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])


                         

            
                