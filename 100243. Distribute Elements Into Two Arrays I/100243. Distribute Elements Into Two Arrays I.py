from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        for elm in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(elm)
            else:
                arr2.append(elm)
        return arr1+arr2

sln=Solution()
assert [5,3,4,8]==sln.resultArray(nums = [5,4,3,8])   
assert [2,3,1]==sln.resultArray(nums = [2,1,3])            