from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        prefixSum=[capacity[0]]
        for i in range(1,len(capacity)):
            prefixSum.append(prefixSum[-1]+capacity[i])
        appleSum=sum(apple)
        for i in range(0,len(capacity)):
            if appleSum <= prefixSum[i]:
                return i+1
        return len(capacity)
    
sln=Solution()
assert 5==sln.minimumBoxes(apple = [9,8,8,2,3,1,6], capacity = [10,1,4,10,8,5])
assert 4==sln.minimumBoxes(apple = [5,5,5], capacity = [2,4,2,7])
assert 2==sln.minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2])
            
        
        