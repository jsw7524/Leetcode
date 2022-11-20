# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
import bisect
from typing import Optional, List

class Solution:
    def __init__(self) -> None:
        self.data=[]
        
    def inorderTraveling(self, node):
        if node.left!=None:
            self.inorderTraveling(node.left)
        self.data.append(node.val)
        if node.right!=None:
            self.inorderTraveling(node.right)        
    
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.inorderTraveling(root)
        self.data.append(10**7)
        result=[]
        for q in queries:
            minI=self.data[bisect.bisect_right(self.data, q)-1]
            maxI=self.data[bisect.bisect_left(self.data, q)]
            result.append(( -1 if minI == 10**7 else minI, -1 if maxI == 10**7 else maxI))
        return result
    

test=[1,2,4,6,9,13,14,15]
pp=1