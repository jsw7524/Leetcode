from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==0:
            return nums[0]
        elif n==1 and k%2==1:
            return -1
        elif k==1:
            return nums[1]
        elif n > k:
            return max(max(nums[:k-1]),nums[k])
        elif n==k:
            return max(nums[:k-1])    
        else: # n < k
            return max(nums)     
        
sln=Solution()

assert -1==sln.maximumTop(nums = [18], k = 3)

assert 5==sln.maximumTop(nums = [5,2,2,4,0,6], k = 4)
assert -1==sln.maximumTop(nums = [2], k = 1)
assert 91==sln.maximumTop([91,98,17,79,15,55,47,86,4,5,17,79,68,60,60,31,72,85,25,77,8,78,40,96,76,69,95,2,42,87,48,72,45,25,40,60,21,91,32,79,2,87,80,97,82,94,69,43,18,19,21,36,44,81,99],2)

