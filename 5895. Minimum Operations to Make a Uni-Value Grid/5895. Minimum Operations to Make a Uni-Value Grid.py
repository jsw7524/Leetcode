from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_list = [item for sublist in grid for item in sublist]
        avg=sum(flat_list)/len(flat_list)
        minElement = min(flat_list)
        maxElement = max(flat_list)
        
        minUniValue= x * ((avg-minElement)//x)+minElement
        maxUniValue= maxElement - x * ((maxElement-avg)//x)
        
        for e in flat_list:
            if abs(e-minUniValue) % x != 0:
                return -1
        
        minOp=2**31-1
        counter=0
        while True:
            for e in flat_list:
                counter += abs(e-minUniValue)//x
            if minOp > counter:
                minOp=counter
                counter=0
                minUniValue-=x
            else:
                break
        counter=0        
        while True:
            for e in flat_list:
                counter += abs(e-maxUniValue)//x
            if minOp > counter:
                minOp=counter
                counter=0
                maxUniValue+=x
            else:
                break                    
        return int(minOp)
                
        
sln=Solution()
assert 4==sln.minOperations(grid = [[2,4],[6,8]], x = 2)
assert 5==sln.minOperations(grid = [[1,5],[2,3]], x = 1)
assert -1==sln.minOperations(grid = [[1,2],[3,4]], x = 2)
assert 25==sln.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92)
assert 12==sln.minOperations(grid = [[931,128],[639,712]], x = 73)