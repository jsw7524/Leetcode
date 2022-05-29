from typing import List


class Solution:
    def IsNonDecreasing(self, start, nums):
        previous=start
        for k in nums:
            if previous > k:
                return False
            previous=k
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=2:
            return True
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                #case 1: nums[i] is too small                
                case1=self.IsNonDecreasing(nums[i-1], nums[i+1:])
                #case 2: nums[i-1] is too big       
                case2=self.IsNonDecreasing(nums[i-2] if i-2 >=0 else -10**5, nums[i:])
                return case1 or case2
        return True

sln=Solution()
assert True==sln.checkPossibility(nums = [3,1])
assert True==sln.checkPossibility(nums = [4,2,3])
assert False==sln.checkPossibility(nums = [1,2,3,422,115,6,7,8,9])
assert False==sln.checkPossibility(nums = [1,2,3,-422,-115,6,7,8,9])
assert True==sln.checkPossibility(nums = [1,2,3,4,115,6,7,8,9])
assert True==sln.checkPossibility(nums = [1,2,3,4,5,6,7,8,9])
assert False==sln.checkPossibility(nums = [4,2,1])

            
        
        