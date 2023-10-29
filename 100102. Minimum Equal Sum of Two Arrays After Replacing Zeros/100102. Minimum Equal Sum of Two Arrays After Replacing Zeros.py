from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1Zero=sum([ 1 for n in nums1 if n==0])
        n2Zero=sum([ 1 for n in nums2 if n==0])
        n1Sum=sum(nums1)+n1Zero
        n2Sum=sum(nums2)+n2Zero
        if n1Sum > n2Sum:
            if n2Zero > 0:
                return n1Sum
            else:
                return -1
        elif n2Sum > n1Sum:
            if n1Zero > 0:
                return n2Sum
            else:
                return -1
        return n1Sum

sln=Solution()
assert -1==sln.minSum(nums1 = [2,0,2,0], nums2 = [1,4])
assert 12==sln.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0])
            
            
        