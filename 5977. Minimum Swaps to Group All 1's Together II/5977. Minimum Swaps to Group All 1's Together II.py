from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numsLength=len(nums)
        oneLength=sum(nums)
        window=sum(nums[:oneLength])
        head=0
        minMove=oneLength-window
        for i in range(oneLength,numsLength+oneLength):
            window=window+nums[i%numsLength]-nums[head%numsLength]
            if minMove > oneLength-window:
                minMove=oneLength-window
            head+=1
        return minMove
    
sln=Solution()
assert 0==sln.minSwaps(nums = [1,1,0,0,1])
assert 1==sln.minSwaps(nums = [0,1,0,1,1,0,0])      
assert 2==sln.minSwaps(nums = [0,1,1,1,0,0,1,1,0])
