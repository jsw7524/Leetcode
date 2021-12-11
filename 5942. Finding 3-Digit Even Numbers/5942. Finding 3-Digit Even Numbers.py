from itertools import combinations
from typing import List 

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        record=[0] * len(digits)
        result=set()
        for i in range(len(digits)):
            if record[i] == 0:
                record[i] = 1
                for j in range(len(digits)):
                    if record[j] == 0:
                        record[j] = 1
                        for k in range(len(digits)):
                            if record[k] == 0:
                                if digits[i] != 0 and digits[k] not in [1,3,5,7,9]:
                                    result.add(digits[i]*100+digits[j]*10+digits[k])
                        record[j] = 0
                record[i] = 0                 
        return sorted([r for r in result])   
                             
sln=Solution()
assert [222,228,282,288,822,828,882]==sln.findEvenNumbers(digits = [2,2,8,8,2])
assert [102,120,130,132,210,230,302,310,312,320]==sln.findEvenNumbers(digits = [2,1,3,0])
assert []==sln.findEvenNumbers(digits = [3,7,5])        
assert [200]==sln.findEvenNumbers(digits = [0,2,0,0])     
assert []==sln.findEvenNumbers(digits = [0,0,0])   