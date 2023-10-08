from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        startTimes = []
        for start in processorTime:
            startTimes.append(start)
            startTimes.append(start)
            startTimes.append(start) 
            startTimes.append(start)  
        startTimes.sort()
        tasks.sort(reverse=True)
        totalTimes=[]
        for i in range(len(startTimes)):
            totalTimes.append(startTimes[i]+tasks[i])
        return max(totalTimes)
                                     
sln=Solution()
assert 23==sln.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3])
assert 16==sln.minProcessingTime(processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5])