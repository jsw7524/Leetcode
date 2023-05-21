class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n=len(s)
        if n%2 == 0 :
            front=s[:n//2]
            rear=s[n//2:]
        else:
            front=s[:n//2]
            rear=s[(n//2)+1:]
            
        result=[]
        for f, r in zip(front,rear[::-1]):
            if r > f:
                result.append(f)
            else:
                result.append(r)
                
        if n%2 == 0 :
            return ''.join(result) + ''.join(result[::-1])
        else:
            return ''.join(result) + s[n//2] +''.join(result[::-1])  

sln=Solution()
assert "efcfe"==sln.makeSmallestPalindrome( s = "egcfe")
assert "abba"==sln.makeSmallestPalindrome( s = "abcd")
assert "neven"==sln.makeSmallestPalindrome( s = "seven")