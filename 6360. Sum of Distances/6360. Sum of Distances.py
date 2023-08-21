import bisect
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dictNums={}
        dictPreSum={}
        lenNums=len(nums)
        for i, n in enumerate(nums):
            if n not in dictNums:
                dictNums[n]=[]
                dictPreSum[n]=[0]
            dictNums[n].append(i)
            dictPreSum[n].append(dictPreSum[n][-1]+i)

        result=[]
        for i, n in enumerate(nums):
            if len(dictNums[n]) == 1:
                result.append(0) 
            else:
                j=bisect.bisect_left(dictNums[n],i)
                soD=(j*i - dictPreSum[n][j]) + ((dictPreSum[n][-1]- dictPreSum[n][j])- ((len(dictPreSum[n])-j-1)*i))
                result.append(soD) 
        return result

sln=Solution()
assert [0,0,0,0,0,0,3,2,3]==sln.distance(nums = [0,5,3,1,2,8,6,6,6])
assert [0,0,0]==sln.distance(nums = [0,5,3])
assert [5,0,3,4,0]==sln.distance(nums = [1,3,1,1,2])