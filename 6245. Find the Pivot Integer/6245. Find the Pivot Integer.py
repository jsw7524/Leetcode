class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixSum=[0]
        for i in range(1,n+1):
            tmp=prefixSum[-1]+i
            prefixSum.append(tmp)
            
        for i in range(1,n+1):
            if prefixSum[i] == prefixSum[n]-prefixSum[i]+i:
                return i
        return -1
    
sln=Solution()
assert -1==sln.pivotInteger(n = 4)
assert 1==sln.pivotInteger(n = 1)
assert 6==sln.pivotInteger(n = 8)