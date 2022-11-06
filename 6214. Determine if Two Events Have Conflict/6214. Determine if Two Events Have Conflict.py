from typing import List

class Solution:
    def convertToMinutes(self, hhmm:str)->int:
        hh, mm = hhmm.split(':')
        return 60 * int(hh) + int(mm)
    
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        startTime1=self.convertToMinutes(event1[0])
        endTime1=self.convertToMinutes(event1[1])      
        startTime2=self.convertToMinutes(event2[0])
        endTime2=self.convertToMinutes(event2[1])    
        if startTime1 > startTime2:
            tmp1, tmp2 = startTime2, endTime2
            startTime2, endTime2 = startTime1, endTime1   
            startTime1, endTime1 = tmp1, tmp2
        
        if startTime2 <= endTime1:
            return True
        return False

sln=Solution()

assert True==sln.haveConflict(event1 =["05:10","15:05"], event2 = ["14:59","19:17"])
assert False==sln.haveConflict(event1 =["14:13","22:08"], event2 = ["02:40","08:08"])
assert False==sln.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"])
assert True==sln.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"])
assert True==sln.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])