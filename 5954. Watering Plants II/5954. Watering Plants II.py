from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        canAlice=capacityA
        canBob=capacityB
        lenPlants=len(plants)
        left=0
        right=lenPlants-1
        refill=0       
        while left < right:
            if plants[left] > canAlice:
                canAlice=capacityA
                refill+=1
            canAlice-=plants[left]

            if plants[right] > canBob:
                canBob=capacityB
                refill+=1
            canBob-=plants[right]
            left+=1
            right-=1
        if left == right: #only for odd number of plants
            if plants[left] > max(canAlice, canBob):
                refill+=1
        return refill
    
sln=Solution()
assert 1==sln.minimumRefill(plants = [2,2,3,3], capacityA = 5, capacityB = 5)
assert 2==sln.minimumRefill(plants = [2,2,3,3], capacityA = 3, capacityB = 4)
assert 0==sln.minimumRefill(plants = [5], capacityA = 10, capacityB = 8)
assert 2==sln.minimumRefill(plants = [1,2,4,4,5], capacityA = 6, capacityB = 5)
assert 1==sln.minimumRefill(plants = [2,2,5,2,2], capacityA = 5, capacityB = 5)