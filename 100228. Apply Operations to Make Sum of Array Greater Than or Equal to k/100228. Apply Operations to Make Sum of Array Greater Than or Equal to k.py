import math
class Solution:
    def minOperations(self, k: int) -> int:
        add=math.sqrt(k)
        way1=(math.ceil(math.sqrt(k))-1) + (math.ceil(k/math.ceil(math.sqrt(k)))-1)
        way2=(math.floor(math.sqrt(k))-1) + (math.ceil(k/math.floor(math.sqrt(k)))-1)
        return min(way1,way2)
    
sln=Solution()
assert 1==sln.minOperations(k=2)
assert 6==sln.minOperations(k=13)
assert 4==sln.minOperations(k=7)
assert 4==sln.minOperations(k=9)
assert 0==sln.minOperations(k=1)
assert 5==sln.minOperations(k=11)
        