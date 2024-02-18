from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n=len(nums)
        m=len(pattern)
        result=0
        for i in range(n-m):
            for k in range(m):
                if nums[i+k+1] - nums[i+k] > 0 and pattern[k]==1:
                    pass
                elif nums[i+k+1] - nums[i+k] == 0 and pattern[k]==0:
                    pass                
                elif nums[i+k+1] - nums[i+k] < 0 and pattern[k]==-1:
                    pass
                else:
                    break
            else:
                result+=1
        return result
            
sln=Solution()
assert 2==sln.countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])      
assert 4==sln.countMatchingSubarrays( nums = [1,2,3,4,5,6], pattern = [1,1])      