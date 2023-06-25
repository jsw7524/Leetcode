class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
    
sln=Solution()
assert 2==sln.minimizedStringLength(s = "dddaaa")
assert 3==sln.minimizedStringLength(s = "cbbd")
assert 3==sln.minimizedStringLength(s = "aaabc")