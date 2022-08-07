from typing import List

class Solution:
    def backTracking(self, graph, node):
        if node in self.prohibited:
            return
        self.counter+=1
        self.visited[node]=1
        for nextNode in graph[node]:
            if nextNode not in self.visited:
                self.backTracking(graph, nextNode)

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.counter=0
        self.visited={}
        graph={}
        self.prohibited={r:1 for r in restricted}
        for e in edges:
            if e[0] not in graph:
                graph[e[0]]=[]
            if e[1] not in graph:
                graph[e[1]]=[]
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        self.backTracking(graph, 0)
        return self.counter

sln=Solution()
assert 1==sln.reachableNodes(n = 2, edges = [[0,1]],restricted =[1])
assert 4==sln.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5])
assert 3==sln.reachableNodes(n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1])
        
        