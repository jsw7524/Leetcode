from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        ptr=head
        while ptr != None:
            length+=1
            ptr=ptr.next
        if length == 1:
            head=None
            return head
            
        target = length//2
        ptr2=head
        previous=None
        for i in range(target):
            previous=ptr2
            ptr2=ptr2.next
        previous.next=ptr2.next
        return head
            