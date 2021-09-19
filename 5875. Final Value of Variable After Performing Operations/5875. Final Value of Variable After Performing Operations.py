from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for op in operations:
            if op in ["++X","X++"]:
                x+=1
            else:
                x-=1
        return x
    
sln=Solution()
assert 1==sln.finalValueAfterOperations(operations = ["--X","X++","X++"])
assert 3==sln.finalValueAfterOperations(operations = ["++X","++X","X++"])
assert 0==sln.finalValueAfterOperations(operations = ["X++","++X","--X","X--"]) 