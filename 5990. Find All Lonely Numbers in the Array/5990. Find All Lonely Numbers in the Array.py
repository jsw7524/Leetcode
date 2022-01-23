from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.insert(0,-1000)
        nums.append(10**7)
        result=[]
        for i, n in enumerate(nums[:-1]):
            if nums[i-1] < n-1 and n+1 < nums[i+1]:
                result.append(n)
        return result
    
sln = Solution()
assert [8,10]==sln.findLonely(nums = [10,6,5,8])
assert [1,5]==sln.findLonely( nums = [1,3,5,3])