from typing import List

class Solution:
    
    def DFS(self, root) -> int:
        self.graph[root][2]=True #visited
        for nextNode in self.graph[root][0]:
            if self.graph[nextNode][2]==False:
                subtreeSize=self.DFS(nextNode)
                self.graph[root][1].append(subtreeSize)
        return 1+sum(self.graph[root][1])
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        self.graph={}
        for a,b in edges:
            if a not in self.graph:
                self.graph[a]=[[],[],False]
            self.graph[a][0].append(b)    
            if b not in self.graph:
                self.graph[b]=[[],[],False]               
            self.graph[b][0].append(a)
        self.DFS(0)
        result=0
        for n in self.graph.keys():
            if len(self.graph[n][1])==0:
                result+=1
            elif  all(x == self.graph[n][1][0] for x in self.graph[n][1]):
                result+=1
        return result
            
sln= Solution()
assert 6==sln.countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]])
assert 12==sln.countGoodNodes(edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]])
assert 6==sln.countGoodNodes(edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]])  
assert 7==sln.countGoodNodes(edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])               
            