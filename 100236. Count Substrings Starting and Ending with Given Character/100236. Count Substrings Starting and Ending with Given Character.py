class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        frq=s.count(c)
        return (1+frq)*frq//2
    
sln=Solution()
assert 6==sln.countSubstrings(s = "zzz", c = "z")
assert 6==sln.countSubstrings(s = "abada", c = "a")