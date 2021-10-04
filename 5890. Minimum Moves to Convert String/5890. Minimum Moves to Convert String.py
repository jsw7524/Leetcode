class Solution:
    def minimumMoves(self, s: str) -> int:
        i=0
        counter=0
        while i < len(s):
            if s[i]=='X':
                i+=3
                counter+=1
            else:
                i+=1
        return counter
    
sln=Solution()
assert 2==sln.minimumMoves(s = "XXOX")
assert 1==sln.minimumMoves(s = "XXX")
assert 0==sln.minimumMoves(s = "OOOO")