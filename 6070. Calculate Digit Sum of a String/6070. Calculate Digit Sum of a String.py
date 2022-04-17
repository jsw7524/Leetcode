class Solution:
    
    def calculate(self, s: str, k) :
        lenS=len(s)
        groups=[s[i:i+k] for i in range(0, len(s), k)]
        groupsSum=[ str(sum([ int(d) for d in g])) for g in groups]
        return ''.join(groupsSum)
            
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s=self.calculate(s, k)
        return s
    
sln=Solution()
assert "135"==sln.digitSum(s = "11111222223", k = 3)
assert "000"==sln.digitSum(s = "00000000", k = 3)
assert "1"==sln.digitSum(s = "1", k = 2)