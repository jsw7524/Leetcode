from typing import List


class MaxHeap:

    def __init__(self, data):
        self.heap = [0]
        self.heap.extend(data)
        self.size = len(self.heap)-1

        for i in range(self.size//2, 0, -1):
            self.goDown(i)
      
    def goUp(self, i):
        while i > 1:
            if  self.heap[i] > self.heap[i//2]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            else:
                break
            i = i//2

    def goDown(self, i):
        while 2*i <= self.size:
            maxChild = 2*i
            if 2*i+1 <= self.size:
                if self.heap[2*i] <= self.heap[2*i+1]:
                    maxChild = 2*i+1
            elif 2*i <= self.size:
                maxChild = 2*i
            else:
                return
            
            if self.heap[i] < self.heap[maxChild]:
                self.heap[i], self.heap[maxChild] = self.heap[maxChild], self.heap[i]
                i = maxChild
            else:
                return            

                
    def peek_max(self):
        return self.heap[1]

    def pop_max(self):
        maxVal=self.heap[1]
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.heap.pop()
        self.size -= 1
        #Sink 
        self.goDown(1)
        return maxVal

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        #Float up
        self.goUp(self.size)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myMaxHeap=MaxHeap(nums)
        for i in range(k):
            val=myMaxHeap.pop_max()
        return val
