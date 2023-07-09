from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length=len(nums)
        Longest = 0
        for l in range(length):
            for r in range(l, length):
                tmp=0
                oddEven=0 
                for i in range(l, r+1):
                    if nums[i] <= threshold and nums[i] % 2  == oddEven:
                        tmp+=1
                        oddEven=(oddEven+1)%2
                    else:
                        break
                Longest=max(Longest, tmp)
        return Longest

sln=Solution()
assert 3==sln.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4)
assert 1==sln.longestAlternatingSubarray(nums = [1,2], threshold = 2)
assert 3==sln.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5)