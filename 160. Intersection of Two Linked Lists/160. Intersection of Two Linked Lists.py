class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        info={}
        current=headA
        while current != None:
            info[id(current)]=current
            current=current.next
        
        current=headB       
        while current != None:
            if id(current) in info:
                return current
            current=current.next
        return None
        