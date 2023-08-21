from typing import List

class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def countBeautifulPairs(self, nums: List[int]) -> int:
        length=len(nums)
        result=0
        for i in range(length):
            for j in range(i+1,length):
                if 1==self.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1])):
                    result+=1
        return result

sln=Solution()
assert 2==sln.countBeautifulPairs(nums = [11,21,12])
assert 5==sln.countBeautifulPairs(nums = [2,5,1,4])
                    
                