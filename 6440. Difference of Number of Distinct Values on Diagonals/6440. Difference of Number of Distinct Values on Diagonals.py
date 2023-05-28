from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        diagonals={}
        pos={}
        m=len(grid)
        n=len(grid[0])
        for r in range(m):
            for c in range(n):
                #y = x + offset => offset = y-x
                if r-c not in diagonals:
                    diagonals[r-c]=[]
                diagonals[r-c].append(grid[r][c])
                pos[(r,c)]=len(diagonals[r-c])-1
        answer=[]
        for r in range(m):
            tmp=[]
            for c in range(n):
                topleft=diagonals[r-c][:pos[(r,c)]]
                bottomright=diagonals[r-c][pos[(r,c)]+1:]
                tmp.append(abs(len(set(topleft)) - len(set(bottomright))))
            answer.append(tmp)
        return answer

sln=Solution()
assert [[0]]==sln.differenceOfDistinctValues(grid = [[1]])
assert [[1,1,0],[1,0,1],[0,1,1]]==sln.differenceOfDistinctValues(grid = [[1,2,3],[3,1,5],[3,2,1]])

                        
                    
                
                
                