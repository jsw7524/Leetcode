from typing import List

class Solution:
    def makeLetter(self, n, font, background):
        img = [[background for x in range(n)] for y in range(n)]
        #\
        for i in range(n//2):
            img[i][i]=font
        #/
        for i in range(n//2):
            img[i][n-i-1]=font
        #|
        for i in range(n//2, n):
            img[i][n//2]=font
        return img  
    
    def checkDiff(self, n, image1, image2):
        diff=0
        for y in range(n):
            for x in range(n):
                if image1[y][x] != image2[y][x]:
                    diff+=1
        return diff
        
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n=len(grid)
        para=[(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
        result=[]  
        for f, b in para:
            r=self.checkDiff(n, grid, self.makeLetter(n, f, b))
            result.append(r)
        return min(result)
        
sln=Solution()
assert 12==sln.minimumOperationsToWriteY(grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])
assert 3==sln.minimumOperationsToWriteY(grid = [[1,2,2],[1,1,0],[0,1,0]])
        
        