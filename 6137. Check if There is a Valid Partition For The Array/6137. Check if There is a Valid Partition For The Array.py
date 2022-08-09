from typing import List


class Solution:
    def backTracking(self, i):
        if i in self.table:
            return  self.table[i]
        if i==self.n:
            return True
        if i < self.n:
            result=False
            if self.nums[i] == self.nums[i+1]:
                result|=self.backTracking(i+2)
            if self.nums[i] == self.nums[i+1] == self.nums[i+2]:
                result|=self.backTracking(i+3)            
            if self.nums[i] == self.nums[i+1]-1 == self.nums[i+2]-2:
                result|=self.backTracking(i+3)
            self.table[i]=result
            return result
        return False             
    
    def validPartition(self, nums: List[int]) -> bool:
        self.n=len(nums)       
        self.table={}     
        self.nums=nums
        nums.append(10**6+10)
        nums.append(10**6+20)        
        nums.append(10**6+30)
        return self.backTracking(0)
                
sln=Solution()
assert False==sln.validPartition(nums = [1,1,1,2])
assert True==sln.validPartition(nums = [4,4,4,5,6])
                  