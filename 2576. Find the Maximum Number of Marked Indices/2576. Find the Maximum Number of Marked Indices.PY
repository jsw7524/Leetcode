from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if 2 * nums[left] <= nums[right]:
                count += 1
                left += 1
                right -= 1
            else:
                right -= 1
        return count

sln=Solution()
assert 2==sln.maxNumOfMarkedIndices(nums = [3,5,2,4])
assert 26==sln.maxNumOfMarkedIndices(nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40])
assert 4==sln.maxNumOfMarkedIndices(nums = [3,5,2,4,3,5,2,4])
assert 0==sln.maxNumOfMarkedIndices(nums = [7,6,8])
assert 4==sln.maxNumOfMarkedIndices(nums = [9,2,5,4])

                
            
        