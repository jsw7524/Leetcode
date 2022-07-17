from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        records={}
        for n in nums:
            if n not in records:
                records[n]=0
            records[n]+=1
        pairs=sum([ v//2 for v in records.values()])
        remain=sum([ r%2 for r in records.values()])
        return [pairs, remain]

sln=Solution()
assert [0,1]==sln.numberOfPairs(nums = [0])
assert [1,0]==sln.numberOfPairs(nums = [1,1])
assert [3,1]==sln.numberOfPairs(nums = [1,3,2,1,3,2,2])