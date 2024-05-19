from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digitLen=len(str(nums[0]))
        record={ i:{ str(d):0 for d in range(10)} for i in range(digitLen)}
        for n in nums:
            strN=str(n)
            for i in range(digitLen):
                record[i][strN[i]]+=1
        answer=0
        for i in range(digitLen):
            for j in range(10):
                for k in range(j+1,10):
                    answer+=record[i][str(j)]*record[i][str(k)]
        return answer
    
sln=Solution()
assert 0==sln.sumDigitDifferences(nums = [10,10,10,10])
assert 4==sln.sumDigitDifferences(nums = [13,23,12])