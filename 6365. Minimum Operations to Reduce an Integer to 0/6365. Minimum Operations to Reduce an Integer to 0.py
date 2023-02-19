
class Solution:      
    def minOperations(self, n: int) -> int:
        pow2=[ 2**i for i in range(18)]
        answer=0
        while n > 0:
            for i in range(17):
                if pow2[i] <= n <= pow2[i+1]:
                    n=min(abs(n-pow2[i]),abs(n-pow2[i+1]))
                    answer+=1
        return answer
        
sln=Solution()
assert 2==sln.minOperations(n = 9)
assert 3==sln.minOperations(n = 39)
assert 3==sln.minOperations(n = 54)
assert 5==sln.minOperations(n = 7862)
assert 1==sln.minOperations(n = 1)
assert 6==sln.minOperations(n = 5673)
assert 6==sln.minOperations(n = 725)
assert 6==sln.minOperations(n = 725)
assert 8==sln.minOperations(n = 45725)
assert 4==sln.minOperations(n = 453)
assert 3==sln.minOperations(n = 54)

