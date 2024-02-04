import math
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length=len(word)
        answer=0
        for i in range(k,length,k):
            answer+=1
            if word[i:]==word[:length-i]:
                return answer
        return math.ceil(length / k)
            
sln=Solution()
assert 4==sln.minimumTimeToInitialState(word = "abcbabcd", k = 2)
assert 1==sln.minimumTimeToInitialState(word = "abacaba", k = 4)
assert 2==sln.minimumTimeToInitialState(word = "abacaba", k = 3)
