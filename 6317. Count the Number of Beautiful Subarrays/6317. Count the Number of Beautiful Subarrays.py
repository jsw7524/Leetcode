from typing import List

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        length=len(nums)
        num1s = [ bin(n).count('1') for n in nums]
        left, right =0, 1
        intervalSum=num1s[left]
        result=0
        while left < length :
            if left == right:
                left+=1
                right+=2
                if right >= length:
                    right=length-1
                continue
            elif (intervalSum+num1s[right])%2==0:
                intervalSum+=num1s[right]
                right+=1
                if right >= length:
                    right=length-1
                result+=1
            elif (intervalSum+num1s[right])%2==1:
                intervalSum-=num1s[left]
                left+=1
        return result

sln=Solution()
assert 2==sln.beautifulSubarrays(nums = [4,3,1,2,4])
        
              
                
            
                
            
        
