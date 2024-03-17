class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse=s[::-1]
        for i in range(len(s)-1):
            if s[i:i+2] in reverse:
                return True
        return False
    
sln=Solution()
assert False==sln.isSubstringPresent(s = "abcd")
assert True==sln.isSubstringPresent(s = "abcba")
assert True==sln.isSubstringPresent(s = "leetcode")