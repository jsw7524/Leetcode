from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result=''
        i=0
        for elm in nums:
            if '0'==elm[i]:
                result+='1'
            else:
                result+='0'
            i+=1
        return result          
            
        