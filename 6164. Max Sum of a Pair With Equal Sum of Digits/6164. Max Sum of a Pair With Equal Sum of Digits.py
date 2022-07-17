from typing import List

class Solution:
    def digitSum(self, n):
        return sum([int(d) for d in str(n)])
    def maximumSum(self, nums: List[int]) -> int:
        records={}
        for n in nums:
            ds=self.digitSum(n)
            if ds not in records:
                records[ds]=[]
            records[ds].append(n)
        data=([  v for v in records.values() if len(v) >= 2 ])
        if 0==len(data):
            return -1
        tmp=[ sorted(v,reverse=True) for v in data ]
        return max([ d[0] + d[1] for d in tmp])

sln=Solution()
assert 973==sln.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401])

assert -1==sln.maximumSum(nums = [10,12,19,14])
assert 54==sln.maximumSum(nums = [18,43,36,13,7])