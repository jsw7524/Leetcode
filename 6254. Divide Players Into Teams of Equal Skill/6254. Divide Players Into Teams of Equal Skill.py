from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        chemistry = 0
        equalSkill=skill[0]+skill[-1]
        for i in range(n//2):
            if equalSkill != skill[i]+skill[-i-1]:
                return -1
            chemistry+=skill[i]*skill[-i-1]
        return chemistry

sln=Solution()
assert -1==sln.dividePlayers(skill = [1,1,2,3])
assert 12==sln.dividePlayers(skill = [3,4])
assert 22==sln.dividePlayers(skill = [3,2,5,1,3,4])
            