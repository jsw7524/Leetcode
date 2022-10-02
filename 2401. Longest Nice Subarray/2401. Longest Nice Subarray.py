from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        niceSubarray = [nums[0]]
        longest=1
        for n in nums[1:]:
            tmp=0
            for elm in niceSubarray:
                if n & elm != 0:
                    niceSubarray=niceSubarray[:tmp]
                tmp+=1
            niceSubarray.insert(0,n)
            longest=max(longest,len(niceSubarray))
        return longest 
    
sln=Solution()
assert 8==sln.longestNiceSubarray(nums = [84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680])  
assert 3==sln.longestNiceSubarray(nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664])  
assert 1==sln.longestNiceSubarray(nums = [3,1,5,11,13])  
assert 3==sln.longestNiceSubarray(nums = [1,3,8,48,10])    
                
                    
                
            
            