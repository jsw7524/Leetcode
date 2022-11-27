class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sIndex=0
        tIndex=0
        sLen=len(s)
        tLen=len(t)
        while (sIndex < sLen) and (tIndex < tLen):
            if s[sIndex]==t[tIndex]:
                sIndex+=1
                tIndex+=1
            else:
                sIndex+=1
        return tLen-tIndex

sln=Solution()
assert 5==sln.appendCharacters(s = "z", t = "abcde")
assert 0==sln.appendCharacters(s = "abcde", t = "a")
assert 4==sln.appendCharacters(s = "coaching", t = "coding")
      