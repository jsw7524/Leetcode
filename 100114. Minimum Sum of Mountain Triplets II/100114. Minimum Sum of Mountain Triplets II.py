from typing import List
import math

class SparseTableRMQ(object):
    def __init__(self, data, minimum=True) -> None:
        self.func= min if minimum else max
        n=len(data)
        logN=math.ceil(math.log2(n))+1
        self.table=[[data[i] for j in range(logN)] for i in range(n)]
        for j in range(1,logN):    
            for i in range(n):
                if (i+2**(j-1)) < n:
                    self.table[i][j]=self.func(self.table[i][j-1],self.table[i+2**(j-1)][j-1])
                else:
                    self.table[i][j]=self.table[i][j-1]    
        return

    def Query(self, left, right):
        if left==right:
            return self.table[left][0]
        distanceLog=math.floor(math.log2(right-left+1))
        return self.func(self.table[left][distanceLog],self.table[right-(2**distanceLog)+1][distanceLog])

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        stRMQ=SparseTableRMQ(nums ,minimum=True)
        numsLen=len(nums)
        mountainTriplet= 4 * 10 ** 8
        for j in range(1, numsLen-1):
            iNums=stRMQ.Query(0,j-1)
            kNums=stRMQ.Query(j+1,numsLen-1)
            if iNums < nums[j] and kNums < nums[j]:
                mountainTriplet = min(mountainTriplet, iNums+nums[j]+kNums )
        return -1 if mountainTriplet==4 * 10 ** 8 else mountainTriplet
    
sln=Solution()
assert -1==sln.minimumSum(nums = [6,5,4,3,4,5])
assert 13==sln.minimumSum(nums = [5,4,8,7,10,2])
assert 9==sln.minimumSum(nums = [8,6,1,5,3])
                