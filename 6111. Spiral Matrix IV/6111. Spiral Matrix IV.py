# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:     
    def GetDataGenerator(self, node):
        while node != None:
            tmp = node.val
            node=node.next
            if None == node:
                self.isContinued=False
            yield tmp
        yield -1

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        self.isContinued=True
        dataGenerator=self.GetDataGenerator(head)
        matrix= [[-1 for j in range(n)] for i in range(m)]
        y,x=0,-1 
        while self.isContinued: # origin state
            while self.isContinued and x+1<n and matrix[y][x+1]==-1:#right state
                matrix[y][x+1]=next(dataGenerator)
                x=x+1

            while self.isContinued and y+1 < m and matrix[y+1][x]==-1: #down state
                matrix[y+1][x]=next(dataGenerator)
                y=y+1   
                     
            while self.isContinued and x-1 >= 0 and matrix[y][x-1]==-1: #left state
                matrix[y][x-1]=next(dataGenerator)
                x=x-1
                 
            while self.isContinued and y-1 >= 0 and matrix[y-1][x]==-1: #up state
                matrix[y-1][x]=next(dataGenerator)
                y=y-1
                     
        return matrix