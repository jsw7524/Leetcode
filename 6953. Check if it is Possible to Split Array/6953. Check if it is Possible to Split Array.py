from typing import List

class Solution:
    def split(self, nums: List[int], m: int, s: int, e: int) -> bool:
        if (s,e) in self.dp:
            return self.dp[(s,e)]
        if (e-s+1)<=2:
            self.dp[(s,e)]=True
            return True
        for i in range(s+1,e+1): 
            if 1==(i-s) and self.rangeSum(nums,i,e) >=m:
                result=self.split(nums, m, i, e)
            elif self.rangeSum(nums, s, i-1)>=m and 1==(e-i+1):
                result=self.split(nums, m, s, i-1) 
            else:
                if self.rangeSum(nums, s, i-1)<m or self.rangeSum(nums,i,e)<m:
                    continue
                result=self.split(nums, m, s, i-1) and self.split(nums, m, i, e)
            if result==True:
                self.dp[(s,e)]=True
                return True
        self.dp[(s,e)]=False
        return False
    
    def makePrefixSum(self, nums):
        self.prefixSum=[nums[0]]
        for n in nums[1:]:
            self.prefixSum.append(self.prefixSum[-1]+n)
    
    def rangeSum(self, nums, s, e):
        return self.prefixSum[e]-self.prefixSum[s] + nums[s]
                    
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        self.dp={}
        self.makePrefixSum(nums)
        return self.split(nums, m, 0, len(nums)-1)
    
sln=Solution()
assert True==sln.canSplitArray(nums = [2, 1, 1, 3], m = 4)
assert True==sln.canSplitArray(nums = [2, 3, 3, 2, 3], m = 6)
assert False==sln.canSplitArray(nums = [2, 1, 3], m = 5 )
assert True==sln.canSplitArray(nums = [2, 2, 1], m = 4)
        

        
        
        