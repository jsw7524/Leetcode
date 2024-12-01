class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i,s in enumerate(range(10, 0, -1)):
            n-=s
            if n==0:
                if i % 2 ==0:
                    return True
                else:
                    return False
            elif n<0:
                if i % 2 ==0:
                    return False
                else:
                    return True                
        return False
    
sln=Solution()
assert False==sln.canAliceWin(n = 1)
assert True==sln.canAliceWin(n = 12)
            