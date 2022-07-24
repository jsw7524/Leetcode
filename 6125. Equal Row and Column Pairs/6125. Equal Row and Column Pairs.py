from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*A)))
    
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        t=self.transpose(grid)
        pairs=0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k]!=t[j][k]:
                        break
                else:
                    pairs+=1
        return pairs

sln=Solution()
assert 1==sln.equalPairs(grid = [[1]])
assert 3==sln.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
assert 1==sln.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])