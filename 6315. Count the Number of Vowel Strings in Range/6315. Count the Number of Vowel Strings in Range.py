from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result=0
        for i in range(left, right+1):
            w=words[i]
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                result+=1
        return result
    
sln=Solution()
assert 3==sln.vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4)
assert 2==sln.vowelStrings(words = ["are","amy","u"], left = 0, right = 2)