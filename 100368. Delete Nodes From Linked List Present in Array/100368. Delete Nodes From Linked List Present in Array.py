# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def check(self,prev,curr):
        if curr == None:
            return
        
        if curr.val in self.info:
            prev.next=curr.next
            self.check(prev, curr.next)
        else:
            self.check(curr, curr.next)            
        return    
    
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        self.info={ n:1 for n in nums }
        stone = ListNode(-1,head)
        self.check(stone,head)
        return stone.next
        
        
        