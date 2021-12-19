from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            left=0
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    break
                left+=1
                right-=1
            else:
                return s
        return ""

sln=Solution()
assert "ada"==sln.firstPalindrome(words = ["abc","car","ada","racecar","cool"])
assert "racecar"==sln.firstPalindrome(words = ["notapalindrome","racecar"])
assert ""==sln.firstPalindrome(words = ["def","ghi"])