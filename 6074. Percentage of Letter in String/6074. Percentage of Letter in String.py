import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        data=[ 1 if c==letter else 0 for c in s]
        return math.trunc(sum(data)/len(data)*100)
    
sln=Solution()
assert 16==sln.percentageLetter("sgawtb","s")

assert 33==sln.percentageLetter(s = "foobar", letter = "o")
assert 0==sln.percentageLetter(s = "jjjj", letter = "k")

