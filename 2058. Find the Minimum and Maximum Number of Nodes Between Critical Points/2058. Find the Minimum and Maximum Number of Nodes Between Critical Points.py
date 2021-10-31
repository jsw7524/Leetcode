# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        tmp=head
        data=[]
        criticalPoint=[]
        while head != None:
            data.append(head.val)
            head=head.next
            
        for i in range(1,len(data)-1):
            if data[i-1] > data[i] and  data[i] < data[i+1]:
                criticalPoint.append(i)
            if data[i-1] < data[i] and  data[i] > data[i+1]:
                criticalPoint.append(i)                
        if len(criticalPoint) < 2:
            return [-1,-1]
        
        maximumDistance=criticalPoint[-1]-criticalPoint[0]
        
        minimumDistance=10**6
        
        for j in range(1,len(criticalPoint)):
            if minimumDistance > (criticalPoint[j]-criticalPoint[j-1]):
                minimumDistance= (criticalPoint[j]-criticalPoint[j-1])
        
        return [minimumDistance, maximumDistance]
