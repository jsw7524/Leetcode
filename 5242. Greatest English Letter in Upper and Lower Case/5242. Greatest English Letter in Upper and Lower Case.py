class Solution:
    def greatestLetter(self, s: str) -> str:
        for ch in "abcdefghijklmnopqrstuvwxyz"[::-1]:
            if ch.upper() in s and ch in s:
                return ch.upper()
        return ""

sln=Solution()
assert ""==sln.greatestLetter(s = "AbCdEfGhIjK")
assert "R"==sln.greatestLetter(s = "arRAzFif")
assert "E"==sln.greatestLetter(s = "lEeTcOdE")