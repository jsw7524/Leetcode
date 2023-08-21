class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer=0;
        sign=1
        for d in str(n):
            answer+=sign*int(d)
            sign*=-1
        return answer
            
sln=Solution()
assert 0==sln.alternateDigitSum(n = 886996)
assert 1==sln.alternateDigitSum(n = 111)
assert 4==sln.alternateDigitSum(n = 521)