class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.data=[-1]*self.size
        self.head=0
        self.tail=self.size-1
        self.length=0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull()==True:
            return False
        self.tail=(self.tail+1) % self.size
        self.data[self.tail]=value        
        self.length+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        self.data[self.head]=-1
        self.head=(self.head+1)% self.size
        self.length-=1
        return True

    def Front(self) -> int:
        if self.isEmpty() == True:
            return -1        
        return self.data[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty() == True:
            return -1         
        return self.data[self.tail]       

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False        

    def isFull(self) -> bool:
        if self.length == self.size:
            return True
        return False           


def test1():
    #TODO: assert following test case
    #Input
    #["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
    #[[3],[1],[2],[3],[4],[],[],[],[4],[]]
    # Expected
    # [null,true,true,true,false,3,true,true,true,4]
    queue = MyCircularQueue(3)
    
    assert queue.enQueue(1) == True
    assert queue.enQueue(2) == True
    assert queue.enQueue(3) == True
    assert queue.enQueue(4) == False  # Queue is full
    assert queue.Rear() == 3
    assert queue.isFull() == True
    assert queue.deQueue() == True
    assert queue.enQueue(4) == True
    assert queue.Rear() == 4    



if __name__ == "__main__":
    test1()