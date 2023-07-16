from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        numsDict={}
        numsLen=len(nums)
        for d in nums:
            if d not in numsDict:
                numsDict[d]=0    
            numsDict[d]+=1
        dominant = max(numsDict, key=numsDict.get)
        prefix=[1] if nums[0]==dominant else [0]
        for i in range(1, numsLen):
            prefix.append(prefix[i-1])
            if nums[i] == dominant:
                prefix[i]+=1
        for i in range(numsLen):
            if 2*prefix[i] > (i+1) and 2*(prefix[numsLen-1]-prefix[i]) > (numsLen-(i+1)):
                return i
        return -1

sln=Solution()
assert -1==sln.minimumIndex(nums = [3,3,3,3,7,2,2])
assert 4==sln.minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1])
assert 2==sln.minimumIndex(nums = [1,2,2,2])
                

        
            
                
            
        
        
        