from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        for r in matrix:
            checkRow=[]
            for c in r:
                if c in checkRow:
                    return False
                checkRow.append(c)
        checkCol=[]
        
        n=len(matrix)
        for c in range(n):
            checkCol=[]
            for r in range(n):
                if matrix[r][c] in checkCol:
                    return False
                checkCol.append(matrix[r][c])     
        return True 
    
sln=Solution()
assert True==sln.checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]])  
assert False==sln.checkValid(matrix = [[1,1,1],[1,2,3],[1,2,3]])  