class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
    
sln=Solution()
assert 7==sln.theMaximumAchievableX(num = 3, t = 2)
assert 6==sln.theMaximumAchievableX(num = 4, t = 1)