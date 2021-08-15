from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        c=1
        while len(nums) > 0:
            if c==1:
                result.append(nums.pop(0))
            else:
                result.append(nums.pop())
            c*=-1
        return result
                
            
        