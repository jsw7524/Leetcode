from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        record=[0]*101
        for n in set(nums1):
            record[n]+=1
        for n in set(nums2):
            record[n]+=1
        for n in set(nums3):
            record[n]+=1
        result=[]
        for n in range(1,101):
            if record[n]>=2:
                result.append(n)
        return result

sln=Solution()
assert [2,3]==sln.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])
assert [1,2,3]==sln.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2])

                
            
              
            
        