from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i, n in enumerate(nums):
            result.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return result
    
sln=Solution()
assert [1]==sln.distinctDifferenceArray(nums = [3])
assert [-2,-1,0,2,3]==sln.distinctDifferenceArray(nums = [3,2,3,4,2])
assert [-3,-1,1,3,5]==sln.distinctDifferenceArray(nums = [1,2,3,4,5])
            
            

        
        
        