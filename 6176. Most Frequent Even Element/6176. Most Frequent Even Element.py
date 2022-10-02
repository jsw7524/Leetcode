from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        record={}
        for n in nums:
            if n%2==1:
                continue
            if n not in record:
                record[n]=0
            record[n]+=1
        if len(record.values())==0:
            return -1            
        minFreq=max(record.values())
        minN=min([ k for k,v in record.items() if v==minFreq])
        return minN
    
sln=Solution()
assert -1==sln.mostFrequentEven(nums = [29,47,21,41,13,37,25,7])
assert 4==sln.mostFrequentEven(nums = [4,4,4,9,2,4])
assert 2==sln.mostFrequentEven(nums = [0,1,2,2,4,4,1])
        
            