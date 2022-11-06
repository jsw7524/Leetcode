from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        info={}
        record=[0]*(1+10**5)
        for i, n in enumerate(nums):
            if n not in info:
                info[n]=[]
            info[n].append(i)
        tmp=sum(nums[:k] )           
        subarraySum=[(tmp,0,k-1)]
        for i in range(1,len(nums)-k+1):
            tmp-=nums[i-1]
            tmp+=nums[i+k-1]
            subarraySum.append((tmp,i,i+k-1))
        subarraySum.sort(reverse=True)
        #checking distinction
        for ss, start, end in subarraySum:
            disqualified=False
            for i in range(start,end+1):
                counter=0
                for j in info[nums[i]]:
                    if start <= j <=end:
                        counter+=1
                        if counter>=2:
                            disqualified=True
                            break
                if disqualified:
                    break
            else:
                return ss                  
        return 0
            
sln=Solution()
assert 0==sln.maximumSubarraySum(nums = [4,4,4], k = 3)   
assert 15==sln.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)           
