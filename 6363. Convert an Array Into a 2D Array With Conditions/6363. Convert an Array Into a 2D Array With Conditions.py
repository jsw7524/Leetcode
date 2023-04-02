from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        record=[0]*201
        size=len(nums)
        for n in nums:
            record[n]+=1
        result=[]
        while size>0:
            tmp=[]
            for i in range(1,201):
                if record[i] > 0:
                    record[i]-=1
                    tmp.append(i)
                    size-=1
            result.append(tmp)
        return result
    
sln=Solution()
sln.findMatrix(nums = [1,3,4,1,2,3,1])
            
        