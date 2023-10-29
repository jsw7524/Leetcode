from typing import List

class Solution:
    def BFS(self, grid, y, x):
        queue=[(y,x,0)]
        while len(queue)>0:
            nY, nX, step  = queue.pop(0)
            if grid[nY][nX] <= 1:
                if nX-1 >= 0:
                    queue.append((nY, nX-1, step+1)) # type: ignore
                if nX+1 < 3:                
                    queue.append((nY, nX+1, step+1))# type: ignore
                if nY-1 >= 0:
                    queue.append((nY-1, nX, step+1))# type: ignore
                if nY+1 < 3:
                    queue.append((nY+1, nX, step+1))# type: ignore
            else:
                return (nY, nX, step)
                
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ops=0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    nY, nX, step = self.BFS(grid, i, j) # type: ignore
                    grid[i][j]+=1
                    grid[nY][nX]-=1
                    ops+=step
        return ops
                    
    
    
sln=Solution()
assert 7==sln.minimumMoves([[3,2,0],[0,1,0],[0,3,0]])


assert (2,1,3)==sln.BFS([[1,1,0],[1,1,1],[1,2,1]],0,2)
assert 4==sln.minimumMoves([[1,2,2],[1,1,0],[0,1,1]])
assert 4==sln.minimumMoves([[1,3,0],[1,0,0],[1,0,3]])
assert 3==sln.minimumMoves([[1,1,0],[1,1,1],[1,2,1]])



        