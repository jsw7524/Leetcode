class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24
    
sln=Solution()
assert 0==sln.findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11)
assert 20==sln.findDelayedArrivalTime(arrivalTime = 15, delayedTime = 5 )