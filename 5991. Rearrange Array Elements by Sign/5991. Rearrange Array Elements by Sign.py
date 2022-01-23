from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for n in nums:
            if n >= 0:
                pos.append(n)
            else:
                neg.append(n)
        result=[]
        for p in pos:
            result.append(p)
            result.append(neg.pop(0))
        return result

sln=Solution()
assert [3,-2,1,-5,2,-4]==sln.rearrangeArray(nums = [3,1,-2,-5,2,-4])
assert [1,-1]==sln.rearrangeArray(nums = [-1,1])