class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        dir=-1
        pos=0
        for i in range(k):
            if pos==0 or pos==n-1:
                dir*=-1
            pos+=dir
        return pos
    
sln=Solution()
assert 2==sln.numberOfChild(n = 4, k = 2)
assert 2==sln.numberOfChild(n = 5, k = 6)
assert 1==sln.numberOfChild(n = 3, k = 5)