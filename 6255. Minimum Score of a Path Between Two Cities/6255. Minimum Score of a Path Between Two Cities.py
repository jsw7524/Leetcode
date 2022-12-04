from typing import List

class Solution:
    
    def __init__(self) -> None:
        pass
    
    def DFS(self, x):
        if self.record[x]==0:
            self.record[x]=1
            if x not in self.graph:
                return
            for nextNode in self.graph[x]:
                if self.minDis > nextNode[2]:
                    self.minDis=nextNode[2]
                self.DFS(nextNode[1])
            #self.record[x]=0
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.graph={}
        self.minDis=10**5
        for r in roads:
            if r[0] not in self.graph:
                self.graph[r[0]]=[]
            if r[1] not in self.graph:
                self.graph[r[1]]=[]
            self.graph[r[0]].append(r)
            self.graph[r[1]].append([r[1],r[0],r[2]])
        self.record = [0] * (n+1)
        self.DFS(1)
        return self.minDis
    
sln=Solution()

assert 2150==sln.minScore(n = 14, roads = [[2,9,2308],[2,5,2150],[12,3,4944],[13,5,5462],[2,10,2187],[2,12,8132],[2,13,3666],[4,14,3019],[2,4,6759],[2,14,9869],[1,10,8147],[3,4,7971],[9,13,8026],[5,12,9982],[10,9,6459]])

assert 2==sln.minScore(n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]])
assert 5==sln.minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])
        
         
        
            
                
        