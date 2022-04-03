from datetime import timedelta
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hhCurrent, mmCurrent=current.split(":")
        hhCorrect, mmCorrect=correct.split(":")
        
        deltaCurrent = timedelta(hours=int(hhCurrent), minutes=int(mmCurrent))
        deltaCorrect = timedelta(hours=int(hhCorrect), minutes=int(mmCorrect))
        
        answer=0
        
        while deltaCurrent + timedelta(minutes=60) <= deltaCorrect:
            deltaCurrent += timedelta(minutes=60)
            answer+=1
                
        while deltaCurrent + timedelta(minutes=15) <= deltaCorrect:
            deltaCurrent += timedelta(minutes=15)
            answer+=1
            
        while deltaCurrent + timedelta(minutes=5) <= deltaCorrect:
            deltaCurrent += timedelta(minutes=5)
            answer+=1
            
        while deltaCurrent + timedelta(minutes=1) <= deltaCorrect:
            deltaCurrent += timedelta(minutes=1)
            answer+=1
        
        return answer
    
sln=Solution()
assert 3==sln.convertTime(current = "02:30", correct = "04:35")
assert 1==sln.convertTime(current = "11:00", correct = "11:01")