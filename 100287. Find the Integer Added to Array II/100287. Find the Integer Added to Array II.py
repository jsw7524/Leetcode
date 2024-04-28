from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sum1=sum(nums1)
        sum2=sum(nums2)
        n=len(nums1)
        minX=999999999
        dict1={}
        for a in nums1:
            if a not in dict1:
                dict1[a]=0
            dict1[a]+=1
            
        dict2={}            
        for b in nums2:
            if b not in dict2:
                dict2[b]=0
            dict2[b]+=1  
                       
        for i in range(n):
            for j in range(i+1,n):
                if (sum2-(sum1-nums1[i]-nums1[j]))%(n-2) == 0:
                    dict1[nums1[i]]-=1
                    dict1[nums1[j]]-=1
                    x=(sum2-(sum1-nums1[i]-nums1[j]))//(n-2)
                    for v in dict1.keys():
                        if dict1[v]>0:
                            if v+x not in dict2:
                                break
                            if dict1[v] != dict2[v+x]:
                                break
                    else:
                        if minX > x:
                            minX=x
                    dict1[nums1[i]]+=1
                    dict1[nums1[j]]+=1                          
        return minX
    
sln=Solution()
assert 1==sln.minimumAddedInteger([3,0,1,8,9,4,7],[4,10,5,1,8])
assert 0==sln.minimumAddedInteger([0,7,6,5,7,0,6,8,2,7],[6,7,8,0,5,2,7,0])
assert -2==sln.minimumAddedInteger([10,2,8,7,5,6,7,10],[5,8,5,3,8,4])
assert 2==sln.minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7])
assert -2==sln.minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10])
                    
                    
                
        