class Solution:
    def makeFancyString(self, s: str) -> str:
        lenS=len(s)
        if lenS <3:
            return s
        result=[]
        for i in range(lenS-2):
            if s[i] == s[i+1] == s[i+2]:
                continue
            result.append(s[i])
        result.append(s[-2])
        result.append(s[-1])        
        return ''.join(result)
    
sln=Solution()
assert "leetcode"==sln.makeFancyString(s = "leeetcode")
assert "aabaa"==sln.makeFancyString(s = "aaabaaaa")
assert "aab"==sln.makeFancyString(s = "aab")