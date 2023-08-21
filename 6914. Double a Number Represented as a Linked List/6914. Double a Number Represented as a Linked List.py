
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptrStack=[]
        ptr=head
        while ptr is not None:
            ptrStack.append(ptr)
            ptr=ptr.next
            
        carrier=0
        for node in ptrStack[::-1]:
            if 2*node.val >= 10:
                node.val=(2*node.val + carrier)%10
                carrier=1
            else:
                node.val=(2*node.val + carrier)%10
                carrier=0
                
        if 1==carrier:
            head = ListNode(1,head)
        return head             
                
            
            
            