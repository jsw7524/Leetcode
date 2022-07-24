class Solution:
    def repeatedCharacter(self, s: str) -> str:
        record={}
        for c in s:
            if c not in record:
                record[c]=0
            record[c]+=1
            if record[c]==2:
                return c
        return None
    
sln=Solution()
assert "d"==sln.repeatedCharacter(s = "abcdd")
assert "c"==sln.repeatedCharacter(s = "abccbaacz")
            