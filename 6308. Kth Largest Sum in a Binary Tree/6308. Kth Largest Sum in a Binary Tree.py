# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def DFS(self, node, depth, records):
        if depth not in records:
            records[depth]=0
        records[depth]+=node.val   
        if None != node.left:
            self.DFS(node.left, depth+1, records)
        if None != node.right:
            self.DFS(node.right, depth+1, records)            
        return
        
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        records={}
        self.DFS(root, 0, records)
        if records.count < k:
            return -1
        else:
            tmp=sorted(records.items,reverse=True)
            return tmp[k]