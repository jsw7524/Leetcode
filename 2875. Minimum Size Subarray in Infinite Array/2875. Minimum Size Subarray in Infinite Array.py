from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        i, j = 0, 0
        length=len(nums)
        minSubLength=99999999
        #case0:
        if target in nums:
            return 1
        
        #case1: inside nums        
        sumSub=nums[0]
        while i < length and j >= i:
            if sumSub == target:
                minSubLength=min(minSubLength, j-i+1)
                sumSub-=nums[i]
                i+=1
            elif sumSub < target:
                j+=1
                if j >= length:
                    break
                sumSub+=nums[j]
            elif sumSub > target:
                sumSub-=nums[i]
                i+=1
        #case2: cross
        numsSum=sum(nums)
        #repeat=target//numsSum
        #remained=target%numsSum
        suffixSum={}
        tmp=0
        for i in range(length-1,-1,-1):
            tmp+=nums[i]
            suffixSum[tmp]=length-i
        tmp=0
        prefixSum={}
        for i in range(length):
            tmp+=nums[i]
            prefixSum[tmp]=i+1

        for k, v in prefixSum.items():
            if target - k in suffixSum:
                minSubLength=min(minSubLength, v+suffixSum[target - k])
        #case3 
        repeat=target//numsSum
        remained=target%numsSum
        for k, v in prefixSum.items():
            if remained - k in suffixSum:
                minSubLength=min(minSubLength,repeat*length +  v+suffixSum[remained - k])        
        
        #case4
        if (target%numsSum==0):
            repeat=(target - remained) // numsSum
            minSubLength=min(minSubLength, repeat*length)
            
        return -1 if minSubLength==99999999 else minSubLength

sln=Solution()

assert 53==sln.minSizeSubarray(nums = [1,2,2,2,1,2,1,2,1,2,1], target = 83)

assert 9==sln.minSizeSubarray(nums = [2,1,5,7,7,1,6,3], target = 39)

assert -1==sln.minSizeSubarray(nums = [2,4,6,8], target = 3)
assert 2==sln.minSizeSubarray(nums = [1,2,3], target = 5)       
assert 2==sln.minSizeSubarray(nums = [1,1,1,2,3], target = 4)                
            
            