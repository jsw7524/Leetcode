from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested=0
        d=len(batteryPercentages)
        for i in range(d):
            if batteryPercentages[i]>0:
                tested+=1
                for j in range(i+1,d):
                    batteryPercentages[j] = max(batteryPercentages[j]-1,0)
        return tested
    
sln=Solution()
assert 2==sln.countTestedDevices(batteryPercentages = [0,1,2])
assert 3==sln.countTestedDevices(batteryPercentages = [1,1,2,1,3])
                    
                