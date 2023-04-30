from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        location={}
        for y in range(m):
            for x in range(n):
                location[mat[y][x]]=(y, x, mat[y][x])
        columns={c:[] for c in range(n)}
        rows={r:[] for r in range(m)}
        for i,a in enumerate(arr):
            y, x, v = location[a]
            columns[x].append(v)
            rows[y].append(v)  
            if len(columns[x]) == m or len(rows[y]) == n:
                return i
        return -1
    
sln=Solution()
assert 3==sln.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]])
assert 2==sln.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]])