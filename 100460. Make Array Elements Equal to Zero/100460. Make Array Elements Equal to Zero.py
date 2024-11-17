from typing import List

class Solution:
    
    def checkSum(self, nums, dir, pos):
        if (pos == 0 and dir=='L')or (len(nums)-1==pos and dir=='R'):
            return 0
        if dir=='L':
            return sum(nums[:pos])
        elif dir=='R':
            return sum(nums[pos+1:])
        return -1
    
    def countValidSelections(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            sumL=self.checkSum(nums,'L',i)
            sumR=self.checkSum(nums,'R',i)
            
            if sumL == sumR:
                result+=2
            elif sumR - sumL ==1:
                result+=1
            elif sumL - sumR ==1:
                result+=1
        return result
    
sln=Solution()
assert 3==sln.countValidSelections(nums = [16,13,10,0,0,0,10,6,7,8,7])  
assert 0==sln.countValidSelections(nums = [2,3,4,0,4,1,0])  
assert 2==sln.countValidSelections(nums = [1,0,2,0,3])              
                
            
        