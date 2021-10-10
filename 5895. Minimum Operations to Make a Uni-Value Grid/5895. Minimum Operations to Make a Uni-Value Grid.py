from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_list = sorted([item for sublist in grid for item in sublist])
        median=flat_list[len(flat_list)//2]
        minOp=0
        for e in flat_list:
            if abs(e-median) % x !=0:
                return -1
            minOp+=abs(e-median)//x
        return minOp

def main():
    sln=Solution()
    assert 4==sln.minOperations(grid = [[2,4],[6,8]], x = 2)
    assert 5==sln.minOperations(grid = [[1,5],[2,3]], x = 1)
    assert -1==sln.minOperations(grid = [[1,2],[3,4]], x = 2)
    assert 25==sln.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92)
    assert 12==sln.minOperations(grid = [[931,128],[639,712]], x = 73)    
                
if __name__ == '__main__':
    main()

        
