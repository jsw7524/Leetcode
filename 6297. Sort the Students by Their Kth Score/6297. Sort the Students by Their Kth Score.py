from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda r: r[k],reverse=True)
        return score
    
sln=Solution()
assert [[7,5,11,2],[10,6,9,1],[4,8,3,15]]==sln.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)
assert [[5,6],[3,4]]==sln.sortTheStudents(score = [[3,4],[5,6]], k = 0)       