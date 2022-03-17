from typing import List


class Solution:
    
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        result=0
        dictDig={ (y, x):1 for y, x in dig}
        for ly,lx,ry,rx in artifacts:
            for i in range(ly,ry+1):
                for j in range(lx,rx+1):
                    if (i, j) not in dictDig:
                        break
                else:
                    continue
                break
            else:
                result+=1
        return result
    
sln=Solution()
assert 1==sln.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]])
assert 2==sln.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]])