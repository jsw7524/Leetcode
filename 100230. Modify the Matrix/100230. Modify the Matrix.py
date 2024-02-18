
from typing import List

class Solution:
    def findMax(self, data) :
        return max(data)
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        for x in range(n):
            tmp=[]
            for y in range(m):
                tmp.append(matrix[y][x])
            maxValue=self.findMax(tmp)
            for y in range(m):
                if -1==matrix[y][x]:
                    matrix[y][x]=maxValue
        return matrix

sln=Solution()
assert [[3,2],[5,2]]==sln.modifiedMatrix(matrix = [[3,-1],[5,2]])     
assert [[1,2,9],[4,8,6],[7,8,9]]==sln.modifiedMatrix(matrix = [[1,2,-1],[4,-1,6],[7,8,9]])        