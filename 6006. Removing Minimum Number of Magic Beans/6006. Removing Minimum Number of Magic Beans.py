from typing import List

class Solution:
    def minimumRemoval(self, nums: List[int]) -> int:
        lenNums=len(nums)
        nums.sort()
        prefixSum=[0]*(lenNums+1)
        suffixSum=[0]*(lenNums+1)
        tmp=0
        for i in range(lenNums):
            prefixSum[i]=tmp
            tmp+=nums[i]
        prefixSum[-1]=tmp   
         
        tmp=0
        for i in range(lenNums-1,-1,-1):
            suffixSum[i+1]=tmp                
            tmp+=nums[i]            
        suffixSum[0]=tmp

        minValue=10**30        
        for i in range(lenNums):
            if prefixSum[i] + (suffixSum[i] - (lenNums-(i+1)) * nums[i]) -nums[i] < minValue:
                minValue=prefixSum[i] + (suffixSum[i] - (lenNums-(i+1)) * nums[i] -nums[i] )  
        return minValue
    
sln=Solution()
assert 7==sln.minimumRemoval( [2,10,3,2]) #[2,2,3,10]
assert 4==sln.minimumRemoval( [4,1,6,5]) #[1,4,5,6]
assert 0==sln.minimumRemoval( [4])
assert 1==sln.minimumRemoval( [4,5])