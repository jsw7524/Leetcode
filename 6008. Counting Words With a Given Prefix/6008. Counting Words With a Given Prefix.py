from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter=0
        for w in words:
            if w.startswith(pref):
                counter+=1
        return counter

sln=Solution()
assert 2==sln.prefixCount(words = ["pay","attention","practice","attend"], pref = "at")
assert 0==sln.prefixCount(words = ["leetcode","win","loops","success"], pref = "code")