class Solution:
    def GCD(self, x, y):
        if y == 0:
            return x
        else:
            return self.GCD(y, x%y)
    def LCM(self, x, y):
        lcm = (x*y)//self.GCD(x,y)
        return lcm
    
    def smallestEvenMultiple(self, n: int) -> int:
        return self.LCM(2,n)

sln=Solution()
assert 10==sln.smallestEvenMultiple(n = 5)
assert 6==sln.smallestEvenMultiple(n = 6)