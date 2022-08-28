from bisect import bisect
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        tmp=0
        prefixSum=[]
        for n in nums:
            tmp+=n
            prefixSum.append(tmp)
        answer=[]
        for q in queries:
            answer.append(bisect(prefixSum,q))
        return answer
    
sln=Solution()
assert [0]==sln.answerQueries(nums = [2,3,4,5], queries = [1])
assert [2,3,4]==sln.answerQueries(nums = [4,5,2,1], queries = [3,10,21])
            
        