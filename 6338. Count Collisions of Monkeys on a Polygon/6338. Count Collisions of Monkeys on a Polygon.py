class Solution:
    def compute2Power(self, n):
        if n==1:
            return 2
        tmp=(self.compute2Power(n//2)%(1000000007))
        if n%2==0:   
            return (tmp**2)%(1000000007)
        return (2*((tmp**2)%(1000000007)))%(1000000007)
    
    def monkeyMove(self, n: int) -> int:
        # ((2**n)-2)%(7+10**9)
        return (self.compute2Power(n)-2)%(1000000007)
    
sln=Solution()
assert 14==sln.monkeyMove(n = 4)
assert 6==sln.monkeyMove(n = 3)
        