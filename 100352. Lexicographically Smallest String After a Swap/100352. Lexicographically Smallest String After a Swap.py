class Solution:
    def getSmallestString(self, s: str) -> str:
        numbers=[s]
        length=len(s)
        for i in range(1, length):
            if int(s[i])%2 == int(s[i-1])%2:
                numbers.append(s[:i-1] + s[i] + s[i-1] + s[i+1:])
        numbers.sort()
        return numbers[0]
    
sln=Solution()
assert "001"==sln.getSmallestString(s = "001")
assert "43520"==sln.getSmallestString(s = "45320")
                
            