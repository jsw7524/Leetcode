from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[[],[]]
        for n in set(nums1):
            if n not in nums2:
                answer[0].append(n)
        for n in set(nums2):
            if n not in nums1:
                answer[1].append(n)
        return answer

sln=Solution()
assert [[3],[]]==sln.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2])
assert [[1,3],[4,6]]==sln.findDifference(nums1 = [1,2,3], nums2 = [2,4,6])       

        