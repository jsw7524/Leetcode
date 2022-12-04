# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[head.val]
        ptr=head
        while ptr.next != None:
            ptr=ptr.next
            values.append(ptr.val)
            
        maxRight=0
        anchor=ListNode()
        for v in values[::-1]:
            if  v >= maxRight:
                newNode=ListNode(v, anchor.next)
                anchor.next=newNode
            maxRight=max(maxRight,v)                
        return anchor.next
        

            
            
            
            
        
        