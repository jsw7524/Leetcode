from typing import List
import re
import bisect
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        posA=[ m.start() for m in re.finditer(a, s)]
        posB=[ m.start() for m in re.finditer(b, s)]
        
        if len(posA)==0 or len(posB)==0:
            return []
        posA.sort()
        posB.sort()
        result=[]
        for i in posA:
            pivot=bisect.bisect(posB,i)
            
            if pivot == len(posB):
                if abs(posB[pivot-1]-i) <= k:
                    result.append(i)
            elif pivot == 0:
                if abs(posB[pivot]-i) <= k:
                    result.append(i)                              
            else:
                if abs(posB[pivot-1]-i) <= k or abs(posB[pivot]-i) <= k:
                    result.append(i)
        return result
    
sln=Solution()
assert []==sln.beautifulIndices(s = "klxtee", a = "e", b = "klx", k = 2) 

assert []==sln.beautifulIndices(s = "lahhnlwx", a = "hhnlw", b = "ty", k = 6) 
assert [0]==sln.beautifulIndices(s = "abcd", a = "a", b = "a", k = 4) 
assert [16,33]==sln.beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15)
                