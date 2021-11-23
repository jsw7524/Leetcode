from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        prefixSum=[]
        tmp=0
        for i in range(len(plants)):
            tmp+=plants[i]
            prefixSum.append(tmp)
        volume=0
        dist=0
        
        c=capacity
        
        for i in range(len(plants)):
            if prefixSum[i] - volume > c:
                dist+=2*i
                dist+=1
                volume=prefixSum[i]
                c=capacity-plants[i]
            else:
                dist+=1
        return dist
    
sln=Solution()
assert 14==sln.wateringPlants(plants = [2,2,3,3], capacity = 5)
assert 30==sln.wateringPlants(plants = [1,1,1,4,2,3], capacity = 4)
assert 49==sln.wateringPlants(plants = [7,7,7,7,7,7,7], capacity = 8)