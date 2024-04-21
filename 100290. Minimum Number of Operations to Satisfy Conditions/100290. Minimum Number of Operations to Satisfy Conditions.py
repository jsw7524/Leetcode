from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m=len(grid)     #row
        n=len(grid[0])  #col
        info={}
        for x in range(n):        
            info[x]={k:0 for k in range(10)}
            for y in range(m):
                info[x][grid[y][x]]+=1
        
        dp=[ [0 for digit in range(10)] for x in range(n)]
        for digit in range(10):
            dp[0][digit]=m-info[0][digit]
        
        for x in range(1,n):
            for digit in range(10):
                previousMinOp=999999
                for previousDigit in range(10): 
                    if previousDigit!=digit:
                        previousMinOp=min(previousMinOp,dp[x-1][previousDigit])
                dp[x][digit]=m-info[x][digit] + previousMinOp
        return min(dp[-1])

sln = Solution()
assert 3==sln.minimumOperations(grid = [[1,1,1],[0,0,0]])
assert 0==sln.minimumOperations(grid = [[1,6,7,3,0,4,1,3,7,5]])
assert 2==sln.minimumOperations(grid = [[1],[2],[3]])
assert 0==sln.minimumOperations(grid = [[1,0,2],[1,0,2]])
                