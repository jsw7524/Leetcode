from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs.insert(0,[None,0])
        record={}
        previousFinishedTime=0
        for e,t in logs[1:]:
            duration=t-previousFinishedTime
            previousFinishedTime=t
            if e not in record:
                record[e]=0
            if duration > record[e]:
                record[e]=duration
        ans=99999999
        maxWorkTime=0
        for id in record.keys():
            workTime = record[id]
            if workTime > maxWorkTime:
                maxWorkTime=workTime
                ans=id
            if workTime == maxWorkTime:
                if ans > id:
                    ans=id
        return ans

sln=Solution()
assert 0==sln.hardestWorker( n = 2, logs = [[0,10],[1,20]])
assert 3==sln.hardestWorker(n = 26, logs = [[1,1],[3,7],[2,12],[7,17]])
assert 1==sln.hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]])
            
            
        