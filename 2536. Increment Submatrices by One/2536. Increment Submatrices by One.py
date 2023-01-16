from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix=[[0 for x in range(n)] for y in range(n)]       
        diff=[[0 for x in range(n+1)] for y in range(n)]        
        for q in queries:
            y1,x1,y2,x2=q
            for i in range(y1,y2+1):
                diff[i][x1]+=1
                diff[i][x2+1]-=1
        for y in range(n):
            matrix[y][0]+=(diff[y][0]) 
        for x in range(1, n):
            for y in range(n):
                    matrix[y][x]+=(diff[y][x]+matrix[y][x-1])       
        return matrix
                
sln=Solution()
assert [[1,1],[1,1]] ==sln.rangeAddQueries(n = 2, queries = [[0,0,1,1]])   
assert [[1,1,0],[1,2,1],[0,1,1]] ==sln.rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]])             
                
                 
            
            