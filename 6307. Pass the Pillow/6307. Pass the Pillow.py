class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos=1
        dir=1
        for t in range(time):
            if pos == 1:
                dir=1
            if pos == n:
                dir=-1
            pos+=dir
        return pos
                

sln=Solution()
assert 6==sln.passThePillow(n = 8, time = 9)
assert 3==sln.passThePillow(n = 3, time = 2)
assert 2==sln.passThePillow(n = 4, time = 5)
