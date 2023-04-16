from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxScore=0
        maxIndex=0
        divisors.sort()
        for i,d in enumerate(divisors):
            score = 0
            for n in nums:
                if n%d==0:
                    score+=1
            if score > maxScore:
                maxScore=score
                maxIndex=i
        return divisors[maxIndex]

sln=Solution()
assert 24==sln.maxDivScore([73,13,20,6], [56,75,83,26,24,53,56,61])
assert 10==sln.maxDivScore(nums = [12], divisors = [10,16])
assert 5==sln.maxDivScore(nums = [20,14,21,10], divisors = [5,7,5])
assert 3==sln.maxDivScore(nums = [4,7,9,3,9], divisors = [5,2,3])
            
                
        
        