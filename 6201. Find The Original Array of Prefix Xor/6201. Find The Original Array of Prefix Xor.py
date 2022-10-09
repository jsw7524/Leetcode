from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        x=pref[0]
        result=[x]
        for i, p in zip(range(1,len(pref)),pref[1:]):
            tmp=x^p            
            result.append(tmp)
            x=x^tmp
        return result

sln=Solution()
assert [13]==sln.findArray(pref = [13])
assert [5,7,2,3,2]==sln.findArray(pref = [5,2,0,3,1])
        