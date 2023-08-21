class Solution:
    def smallestString(self, s: str) -> str:
        result=[]
        i=0
        n=len(s)
        while i < n and s[i]=='a' :
            result.append('a')
            i+=1
        while i < n and s[i]!='a':
            result.append(chr(ord(s[i])-1))
            i+=1            
        while i < n:
            result.append(s[i])
            i+=1
        if ''.join(result) == s:
            result[-1]='z'
        return ''.join(result)
    
sln=Solution()
assert "z"==sln.smallestString(s = "a")
assert "kddsbncd"==sln.smallestString(s = "leetcode")
assert "abaab"==sln.smallestString(s = "acbbc")
assert "baabc"==sln.smallestString(s = "cbabc")