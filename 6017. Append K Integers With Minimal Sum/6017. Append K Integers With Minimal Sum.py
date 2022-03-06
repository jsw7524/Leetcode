from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        dictInfo={n:1 for n in nums}
        result = (k)*(k+1)//2
        tmp=k+1
        for n in dictInfo.keys():
           if n <= k:
               result-=n    
               while tmp in dictInfo:
                   tmp+=1
               result+=tmp
               tmp+=1                  
        return result
    
sln=Solution()
assert 794==sln.minimalKSum(nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], k = 35)  
assert 23==sln.minimalKSum(nums = [2,3,3,8], k = 5)
assert 3444==sln.minimalKSum(nums = [53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83], k = 76)  
assert 5==sln.minimalKSum(nums = [1,4,25,10,25], k = 2)
assert 25==sln.minimalKSum(nums = [5,6], k = 6)
               
