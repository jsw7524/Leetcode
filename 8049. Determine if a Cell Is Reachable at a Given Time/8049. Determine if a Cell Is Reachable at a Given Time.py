class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy:
            if t==0:
                return True
            return t>=2
        return max(abs(sx-fx),abs(sy-fy))<=t
    
sln=Solution()
assert False==sln.isReachableAtTime(sx = 1, sy = 2, fx = 1, fy = 2, t = 1)
assert False==sln.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3)
assert True==sln.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6)