from typing import List
from itertools import permutations
class Solution:
    
    def GetPairScore(self, students, mentors):
        pairScores={}
        for i, s in enumerate(students):
            for j, m in enumerate(mentors):
                score=0
                for k in range(self.n):
                    if s[k] == m[k]:
                        score+=1
                pairScores[(i,j)]=score
        return pairScores
                
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        self.m=len(students)
        self.n=len(students[0])
        ps=self.GetPairScore(students, mentors)
        maximumCompatibilityScoreSum=0
        for p in permutations(range(0,self.m)):
            tmp=0
            for i in range(self.m):
                tmp+=ps[(i,p[i])]
            if tmp > maximumCompatibilityScoreSum:
                maximumCompatibilityScoreSum = tmp
        return maximumCompatibilityScoreSum
    
sln=Solution()
assert 8==sln.maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]])
assert 0==sln.maxCompatibilitySum(students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]])        
assert 10==sln.maxCompatibilitySum(students = [[0,1,0,1,1,1],[1,0,0,1,0,1],[1,0,1,1,0,0]], mentors = [[1,0,0,0,0,1],[0,1,0,0,1,1],[0,1,0,0,1,1]])    



