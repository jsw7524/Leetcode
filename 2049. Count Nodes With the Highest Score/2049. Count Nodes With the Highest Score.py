from typing import List

class node(object):
    def __init__(self, id):
        self.id=id
        self.left=None
        self.right=None
        self.size=0
        

class Solution:
    
    def TreeTravel(self, x):
        if self.tree[x].left == None and self.tree[x].right == None:
            self.tree[x].size=1
            return 1
        ln, rn = 0, 0
        if self.tree[x].left != None:
            ln=self.TreeTravel(self.tree[x].left)
        if self.tree[x].right != None:
            rn=self.TreeTravel(self.tree[x].right) 
        self.tree[x].size=1+ln+rn 
        return self.tree[x].size
            
    
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        lenParents= len(parents)
        self.tree= [ node(i) for i in range(lenParents)]
        for i in range(1,lenParents):
            if self.tree[parents[i]].left == None:
                self.tree[parents[i]].left=i
            elif self.tree[parents[i]].right == None:
                self.tree[parents[i]].right=i       
        self.TreeTravel(0)
        
        maxScore=0
        counter=0
        for i in range(0, lenParents):
            ln, rn = 1, 1 
            if self.tree[i].left != None:
                ln=self.tree[self.tree[i].left].size
            if self.tree[i].right != None:
                rn=self.tree[self.tree[i].right].size
            remainder= 1 if (lenParents - self.tree[i].size)  == 0  else (lenParents - self.tree[i].size)
            tmp= ln * rn *  remainder           
            if tmp > maxScore:
                maxScore=tmp
                counter=0
            if tmp == maxScore:
                counter+=1
        return counter
        
                
sln=Solution()
assert 3==sln.countHighestScoreNodes(parents = [-1,2,0,2,0])
assert 2==sln.countHighestScoreNodes(parents = [-1,2,0])
assert 2==sln.countHighestScoreNodes(parents = [-1,0])
