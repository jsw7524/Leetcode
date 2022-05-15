from typing import List
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maxValue=0
        if bottom != special[0]:
            special.insert(0, bottom-1)
        if top != special[-1]:
            special.append(top+1)
        for i, n in enumerate(special[:-1]):
            if (special[i+1]-special[i]-1) > maxValue:
                maxValue=(special[i+1]-special[i]-1)
        return maxValue
    
sln=Solution()
assert 3==sln.maxConsecutive(bottom = 2, top = 9, special = [4,6])
assert 0==sln.maxConsecutive(bottom = 6, top = 8, special = [7,6,8])
            

            