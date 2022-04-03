from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        numsLen=len(nums)
        mapInfo=[nums[0]]
        result=0
        for i in range(1,numsLen):
            if nums[i] != nums[i-1]:
                mapInfo.append(nums[i])
            
        m=len(mapInfo)
        for i in range(1,m-1):
            if mapInfo[i]>mapInfo[i-1] and mapInfo[i]>mapInfo[i+1]:
                result+=1
            if mapInfo[i]<mapInfo[i-1] and mapInfo[i]<mapInfo[i+1]:
                result+=1
        
        return result
    
sln=Solution()
assert 3==sln.countHillValley(nums = [2,4,1,1,6,5])
assert 0==sln.countHillValley(nums = [6,6,5,5,4,1])
                
