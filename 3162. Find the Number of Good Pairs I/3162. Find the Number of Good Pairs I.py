from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result=0
        for n1 in nums1:
            for n2 in nums2:
                if n1 % (n2*k)==0:
                    result+=1
        return result
    
sln=Solution()
assert 2==sln.numberOfPairs( nums1 = [1,2,4,12], nums2 = [2,4], k = 3) 
assert 5==sln.numberOfPairs( nums1 = [1,3,4], nums2 = [1,3,4], k = 1) 