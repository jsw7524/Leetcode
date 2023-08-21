from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        k,n=0,0
        for i,r in enumerate(mat):
            if sum(r) > n:
                n=sum(r)
                k=i
        return [k, n]

sln=Solution()
assert [1,2]==sln.rowAndMaximumOnes(mat = [[0,0],[1,1],[0,0]])
assert [1,2]==sln.rowAndMaximumOnes(mat = [[0,0,0],[0,1,1]])      
assert [0,1]==sln.rowAndMaximumOnes(mat = [[0,1],[1,0]])
            
        