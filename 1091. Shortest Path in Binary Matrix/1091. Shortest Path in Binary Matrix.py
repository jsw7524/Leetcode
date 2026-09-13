from typing import List


class Solution:

    def BFS(self, grid, queue):
        height=len(grid)
        width=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)]
        while len(queue) > 0:
            x, y, step = queue.pop(0)
            if x == height-1 and y == width-1:
                return step  
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x >= 0 and new_x < height and new_y >= 0 and new_y < width and grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y, step+1))
                    grid[new_x][new_y] = 1
        return -1
            

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=[]
        if grid[0][0] == 0:
            queue.append((0,0,1))
        else:
            return -1
        return self.BFS(grid, queue)
        