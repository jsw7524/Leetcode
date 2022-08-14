from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        length=len(edges)
        scores=[0]*length
        for i, n in enumerate(edges):
            scores[n]+=i
        maxScore=scores[0]
        maxIndex=0
        for i in range(length):
            if scores[i] > maxScore:
                maxScore=scores[i]
                maxIndex=i
        return maxIndex

sln=Solution()
assert 0==sln.edgeScore(edges = [2,0,0,2])
assert 7==sln.edgeScore(edges = [1,0,0,0,0,7,7,5])
            