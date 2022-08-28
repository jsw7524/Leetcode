from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def makeGraph(self, node , fromVertex):
        if node not in self.graph:
            self.graph[node.val]=[]
        if None != fromVertex:
            self.graph[node.val].append(fromVertex.val)
        if node.left is not None:
            self.graph[node.val].append(node.left.val)
            self.makeGraph(node.left, node)
        if node.right is not None:
            self.graph[node.val].append(node.right.val)
            self.makeGraph(node.right, node)
    
    def longestPath(self, vertex, path):
        if vertex not in self.record:
            self.record[vertex]=0
            
        if 1==self.record[vertex]:
            return path
        self.record[vertex]=1       
        tmp=path
        for nextVertex in self.graph[vertex]:
            if nextVertex in self.record:
                if 1== self.record[vertex]:
                    continue
            tmp=max(tmp, self.longestPath(nextVertex, path+1))
        self.record[vertex]=0
        return tmp
            
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph={}
        self.makeGraph(root,None)
        self.record={}
        print(self.graph)
        return self.longestPath(start, 0)
        