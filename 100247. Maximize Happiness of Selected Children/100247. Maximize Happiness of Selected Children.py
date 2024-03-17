from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result=0
        decrease=0
        for i in range(k):
            if happiness[i]-decrease > 0:
                result+=(happiness[i]-decrease)
                decrease+=1
            else:
                break
        return result
    
sln=Solution()
assert 53==sln.maximumHappinessSum(happiness = [12,1,42], k = 3)
assert 5==sln.maximumHappinessSum(happiness = [2,3,4,5], k = 1)
assert 1==sln.maximumHappinessSum(happiness = [1,1,1,1], k = 2)
assert 4==sln.maximumHappinessSum(happiness = [1,2,3], k = 2)
        