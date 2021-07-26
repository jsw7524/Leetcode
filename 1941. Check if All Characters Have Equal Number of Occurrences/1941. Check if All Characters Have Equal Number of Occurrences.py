class Solution:
    def areOccurrencesEqual(self, s):
        info={}
        for c in s:
            if c not in info:
                info[c]=0
            info[c]+=1
        for c in s:
            if info[c] != info[s[0]]:
                return False
        return True
    
sln=Solution()
assert True==sln.areOccurrencesEqual(s = "abacbc")
assert False==sln.areOccurrencesEqual(s = "aaabb")