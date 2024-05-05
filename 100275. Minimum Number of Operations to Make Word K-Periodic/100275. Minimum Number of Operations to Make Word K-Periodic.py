from collections import Counter
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n=len(word)
        counter=Counter( word[i:i+k]  for i in range(0, n, k))
        kword, frq = (counter.most_common(1))[0]
        return n//k - frq
    
sln=Solution()
assert 3==sln.minimumOperationsToMakeKPeriodic(word = "leetcoleet", k = 2)
assert 1==sln.minimumOperationsToMakeKPeriodic(word = "leetcodeleet", k = 4)