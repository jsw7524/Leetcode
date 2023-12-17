from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(0, len(nums), 3):
            if nums[i] + k  >=  nums[i+1] and nums[i] + k  >=  nums[i+1] and nums[i] + k  >=  nums[i+2]:
                res.append(nums[i : i + 2 + 1])
            else:
                return []
        return res
    
sln=Solution()
assert []==sln.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2],2)
assert []==sln.divideArray(nums = [1,3,3,2,7,3], k = 3)
assert [[1,1,3],[3,4,5],[7,8,9]]==sln.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2)
        
        