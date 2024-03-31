from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        start, end =0, 0
        n = len(nums)
        lengthAS=[]
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                lengthAS.append(end-start+1)
                end+=1
                start=end
            else:
                end+=1
        lengthAS.append(end-start+1)
        result = [ ln*(ln+1)//2 for ln in lengthAS]
        return sum(result)

sln=Solution()
assert 10==sln.countAlternatingSubarrays(nums = [1,0,1,0])
assert 5==sln.countAlternatingSubarrays(nums = [0,1,1,1])
        