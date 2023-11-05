from typing import List

class Tournament:
    def __init__(self,n):
        self.dominator = [i for i in range(n)]

    def findDominator(self,x):
        if self.dominator[x] == x:
            return x
        else:
            self.dominator[x] = self.findDominator(self.dominator[x])
            return self.dominator[x]

    def strength(self, stronger, weaker):    
        self.dominator[weaker]=self.findDominator(stronger) 
        return
    
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        tourney = Tournament(n)
        for stronger, weaker in edges:
            tourney.strength(stronger, weaker)
        dmnt=[ tourney.findDominator(t) for t in range(n)]    
        return dmnt[0] if all(dmnt[0]==i for i in dmnt) else -1
  
sln=Solution()
assert 0==sln.findChampion(n = 3, edges = [[0,1],[2,1],[0,2]]) 
assert 0==sln.findChampion(n = 3, edges = [[0,1],[1,2]]) 
assert 1==sln.findChampion(n = 2, edges = [[1,0]])
assert 0==sln.findChampion(n = 3, edges = [[0,2],[0,1]]) 
assert 0==sln.findChampion(n = 1, edges = []) 
assert -1==sln.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]])
           