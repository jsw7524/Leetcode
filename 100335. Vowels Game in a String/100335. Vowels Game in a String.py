class Solution:
    def doesAliceWin(self, s: str) -> bool:
        counter=0
        for c in s:
            if c in "aeiou":
                counter+=1
        if counter==0:
            return False
        return True
    
sln=Solution()
assert True==sln.doesAliceWin(s = "sloalo")
assert True==sln.doesAliceWin(s = "ifld")
assert False==sln.doesAliceWin(s = "bbcd")
assert True==sln.doesAliceWin(s = "leetcoder")