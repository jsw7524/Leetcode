class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1=s.count('1')
        s0=s.count('0')
        return ''.join(['1' for i in range(s1-1)] + ['0' for i in range(s0)]) +'1'
    
sln=Solution()
assert "1001"==sln.maximumOddBinaryNumber(s = "0101")
assert "001"==sln.maximumOddBinaryNumber(s = "010")