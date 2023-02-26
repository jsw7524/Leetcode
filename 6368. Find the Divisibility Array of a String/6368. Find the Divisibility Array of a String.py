from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remainder=0
        result=[]
        lengthWord=len(word)
        for d in word:
            r=(remainder*10+int(d))%m
            if r==0:
                result.append(1)
            else:
                result.append(0)
            remainder=r
        return result

sln=Solution()
assert [0,1,0,1]==sln.divisibilityArray(word = "1010", m = 10)
assert [1,1,0,0,0,1,1,0,0]==sln.divisibilityArray(word = "998244353", m = 3)
