import bisect
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bit1Info={ i:[-1] for i in  range(32)}
        for i, n in enumerate(nums):
            tmp=n
            bitPosition=0
            while tmp !=0 :
                if tmp%2 == 1:
                    bit1Info[bitPosition].append(i)
                tmp//=2
                bitPosition+=1
        result=[]
        for i, n in enumerate(nums):
            info=[]
            for j in range(32):
                loc=bisect.bisect(bit1Info[j], i)
                if 0!=loc:
                    info.append(bit1Info[j][loc]-i)
            result.append(min(info))

sln=Solution()
sln.longestNiceSubarray(nums = [1,3,8,48,10])
        
                    
                    
                
            
        