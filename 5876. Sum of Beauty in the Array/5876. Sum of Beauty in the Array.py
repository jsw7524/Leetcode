from typing import List

class Solution:
    def PrefixMax(self,nums):
        tmp=[]
        max=0
        for n in nums:
            if n > max:
                max=n
            tmp.append(max)
        return tmp

    def SuffixMin(self,nums):
        tmp=[]
        min=10**7
        for n in nums[::-1]:
            if n < min:
                min=n
            tmp.append(min)
        return list(reversed(tmp))
    
    def sumOfBeauties(self, nums: List[int]) -> int:
        beauty = 0
        prefixMax=self.PrefixMax(nums)
        suffixMin=self.SuffixMin(nums)        
        for i in range(1,len(nums)-1):
            if prefixMax[i-1] < nums[i] < suffixMin[i+1]:
                beauty+=2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty+=1
        return beauty

sln=Solution()
assert 2==sln.sumOfBeauties(nums = [1,2,3])
assert 1==sln.sumOfBeauties(nums = [2,4,6,4])       
assert 0==sln.sumOfBeauties(nums = [3,2,1])      
assert 0==sln.sumOfBeauties([9,9,3,8,7,9,6,10])      