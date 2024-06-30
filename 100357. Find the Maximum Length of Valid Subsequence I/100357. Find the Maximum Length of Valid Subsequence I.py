from typing import List

class Solution:
    
    def firstEvenLocation(self, nums: List[int])-> int:
        for i, num in enumerate(nums):
            if num % 2 == 0:
                return i
        return -1  
          
    def firstOddLocation(self, nums: List[int])-> int:
        for i, num in enumerate(nums):
            if num % 2 == 1:
                return i
        return -1     
    
    def maximumLength(self, nums: List[int]) -> int:
        ee = [n for n in nums if n%2==0]
        oo = [n for n in nums if n%2==1]
        length = len(nums)
        eo=[]      
        fel=self.firstEvenLocation(nums)
        if fel >=0:
            tmp=nums[fel]
            eo.append(nums[fel])        
            for i in range(fel+1,length):
                if (tmp + nums[i])%2==1:
                    tmp=nums[i]
                    eo.append(nums[i])
        oe=[]
        fol=self.firstOddLocation(nums)
        if fol >=0:
            tmp=nums[fol]
            oe.append(nums[fol])        
            for i in range(fol+1,length):
                if (tmp + nums[i])%2==1:
                    tmp=nums[i]
                    oe.append(nums[i])     
        return max(len(ee),len(oo),len(oe),len(eo))
    
sln=Solution()
assert 2==sln.maximumLength(nums = [2,3])
assert 2==sln.maximumLength(nums = [1,3])
assert 6==sln.maximumLength(nums = [1,2,1,1,2,1,2])
assert 4==sln.maximumLength(nums = [1,2,3,4])