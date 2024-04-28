from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sorted(nums2))[0]-(sorted(nums1))[0]
    
sln=Solution()
assert 0==sln.addedInteger( nums1 = [1,1,1,1], nums2 = [1,1,1,1])
assert -5==sln.addedInteger(nums1 = [10], nums2 = [5])
assert 3==sln.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5])