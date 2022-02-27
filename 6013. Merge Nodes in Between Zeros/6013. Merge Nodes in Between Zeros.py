# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        origin=modifiedList=ListNode(0)
        ptr=head.next
        sumSegment=0
        while ptr != None:
            sumSegment+=ptr.val
            if ptr.val == 0:
                modifiedList.next=ListNode(sumSegment)
                modifiedList=modifiedList.next
                sumSegment=0
            ptr=ptr.next
        return origin.next
            
            
            