from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]
        tmp=[s[0]]
        count=1
        for i,c in enumerate(s[1:]):
            if count%k==0:
                result.append(''.join(tmp))
                tmp=[]
                count=0
            tmp.append(c)   
            count+=1  
        if len(tmp)>0 and len(tmp)<=k:
            for i in range(k-len(tmp)):
                tmp.append(fill)
            result.append(''.join(tmp))
        return result

sln=Solution()
assert ["abc","def","ghi"]==sln.divideString(s = "abcdefghi", k = 3, fill = "x")
assert ["abc","def","ghi","jxx"]==sln.divideString(s = "abcdefghij", k = 3, fill = "x")