from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        des=[nums[0]]
        asc=[nums[0]]
        result=1
        for n in nums[1:]:
            if n <= asc[-1]:
                asc.clear()
            asc.append(n)
            if n >= des[-1]:
                des.clear()
            des.append(n)
            result=max(result,len(asc),len(des))
        return result

sln=Solution()
assert 3==sln.longestMonotonicSubarray( nums = [3,2,1])
assert 1==sln.longestMonotonicSubarray( nums = [3,3,3,3])
assert 2==sln.longestMonotonicSubarray( nums = [1,4,3,3,2])

        