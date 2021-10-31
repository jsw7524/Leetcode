class MyCircularDeque:

    def __init__(self, k: int):
        self.data=[-1]*k
        self.k=k
        self.left=0
        self.right=0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.left%self.k]=value        
        self.left-=1

        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.right%self.k]=value        
        self.right+=1

        return True       

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.left+=1
        return True        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right-=1
        return True            

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.left+1)%self.k]   

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.right-1)%self.k]           

    def isEmpty(self) -> bool:
        if (self.right-self.left) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if (self.right-self.left) == self.k:
            return True        
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()