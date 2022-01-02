class Solution:
    def checkString(self, s: str) -> bool:
        stateA=0
        for c in s[::-1]:
            if c == 'a':
                stateA=1
            if stateA == 1 and c =='b':
                return False
        return True

sln = Solution()
assert True==sln.checkString(s = "aaabbb")
assert False==sln.checkString(s = "abab")           
assert True==sln.checkString(s = "bbb")      