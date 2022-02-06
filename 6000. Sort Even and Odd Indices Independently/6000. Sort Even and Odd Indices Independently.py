
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        result=[]
        for i in range(len(odd)):
            result.append(even.pop(0))
            result.append(odd.pop(0))
        if len(even) > 0:
            result.append(even.pop(0))
        return result

sln=Solution()
sln.sortEvenOdd(nums = [5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21])  

assert [2,3,4,1]==sln.sortEvenOdd(nums = [4,1,2,3])
assert [2,1]==sln.sortEvenOdd(nums = [2,1])            
assert [1]==sln.sortEvenOdd(nums = [1])  


  
