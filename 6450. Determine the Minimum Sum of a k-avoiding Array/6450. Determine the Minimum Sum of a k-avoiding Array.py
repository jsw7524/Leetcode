class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        if n >= k//2:
            result = [i for i in range(1,1+k//2)]
            j=0
            while len(result) < n:
                result.append(k+j)
                j+=1
            return sum(result)
        else:
            return sum([i for i in range(1,n+1)])

sln=Solution()

assert 3==sln.minimumSum(n = 2, k = 6)
assert 18==sln.minimumSum(n = 5, k = 4)
            
            