from typing import List

class Solution:
    def __init__(self) -> None:
        self.tempResult=[0]*12
        self.result=[0]*12
        self.maxScore=0
        
    def DFS(self,depth,score,numArrows):
        if depth == 0:
            if score > self.maxScore:
                self.maxScore=score
                self.tempResult[0]=numArrows
                self.result=self.tempResult.copy()
        else:
            # pruning impossible cases
            if self.maxScore >= score + (depth+1)*depth/2:
                return 
            
            # give up k section
            self.tempResult[depth]=0
            self.DFS(depth-1,score,numArrows)

            # win k section    
            if numArrows > self._aliceArrows[depth]:
                self.tempResult[depth]=self._aliceArrows[depth]+1
                self.DFS(depth-1,score+depth,numArrows-(self._aliceArrows[depth]+1))

            #tie
            if numArrows >= self._aliceArrows[depth]:               
                self.tempResult[depth]=self._aliceArrows[depth]
                self.DFS(depth-1,score,numArrows-(self._aliceArrows[depth]))
            return
        
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self._aliceArrows=aliceArrows
        self.DFS(11,0,numArrows)
        return self.result
 


sln=Solution()
#sln.maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0])
sln.maximumBobPoints(numArrows = 71398, aliceArrows = [0,2642,19009,9870,108,11150,10660,3190,5783,3177,2680,3129])        