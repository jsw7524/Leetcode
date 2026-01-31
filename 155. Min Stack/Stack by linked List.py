class Node:
    def __init__(self, value):
        self.val=value
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.anchor=Node(-1)
        self.tail=self.anchor
        self.length=0


    def __str__(self):
        #print("Show Linked List")
        current=self.anchor.next
        result="Show Linked List:"
        while current != None:
            #print(current.val, sep=" ")
            result+=str(current.val)
            result+="->"     
            current=current.next
        result+="None"
        return result
        

    def findNode(self, index):
        current=self.anchor
        for _ in range(index+1):
            current=current.next
        return current       
        
    def get(self, index: int) -> int:
        print("get",index)
        print(self)        
        if index>= self.length: 
            print("index exceeded")     
            return -1       
        target=self.findNode(index)
        return target.val  

    def addAtHead(self, val: int) -> None:
        print("addAtHead",val)        
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        print("addAtTail",val)        
        newNode = Node(val)
        self.tail.next=newNode
        self.tail=newNode
        self.length+=1
        print(self)        

    def addAtIndex(self, index: int, val: int) -> None:
        print("addAtIndex", index, val)
        if index== self.length:
            self.addAtTail(val)
            return 
        if index> self.length:
            print("index exceeded")   
            return
        previous=self.findNode(index-1)
        afterNewOne=previous.next
        newNode=Node(val)
        newNode.next=afterNewOne       
        previous.next=newNode
        self.length+=1
        print(self)

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            print("index exceeded")   
            return 
        print("deleteAtIndex", index)
        previous=self.findNode(index-1)
        delTarget=previous.next
        #檢查要刪除的節點是否為tail，是的話要更新tail
        if delTarget == self.tail:
            self.tail = previous
        # 執行刪除
        if delTarget != None:
            previous.next = delTarget.next
        self.length-=1
        print(self)  


class MinStack:

    def __init__(self):
        self.min=MyLinkedList()
        self.data=MyLinkedList()   
        self.length=0

    def push(self, val: int) -> None:
        print("push")
        if self.length==0:
            self.min.addAtTail(val)
        else:
            self.min.addAtTail(min(self.min.get(self.length-1),val))               
        self.data.addAtTail(val)            
        self.length+=1

    def pop(self) -> None:
        print("pop")
        if self.length==0:
            return None
        self.length-=1    
        self.min.deleteAtIndex(self.length)
        result= self.data.get(self.length)
        self.data.deleteAtIndex(self.length)    
        #return result

    def top(self) -> int:
        print("top")
        return self.data.get(self.length-1)
        

    def getMin(self) -> int:
        print("getMin")        
        if self.length == 0:
            return None
        return self.min.get(self.length-1)
    

def test1():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_4 = obj.getMin()
    assert param_4 == -3
    obj.pop()
    param_3 = obj.top()
    assert param_3 == 0
    param_4 = obj.getMin()
    assert param_4 == -2


def test2():
# ["MinStack","push","push","push","getMin","pop","getMin","pop","getMin","pop","push","push","push","getMin","pop","top","getMin","pop","getMin","pop"]
# [[],[0],[1],[0],[],[],[],[],[],[],[-2],[-1],[-2],[],[],[],[],[],[],[]]    
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    param_4 = obj.getMin()
    assert param_4 == 0
    obj.pop()
    param_4 = obj.getMin()
    assert param_4 == 0
    obj.pop()
    param_4 = obj.getMin()
    assert param_4 == 0
    obj.pop()
    obj.push(-2)
    obj.push(-1)
    obj.push(-2)
    param_4 = obj.getMin()
    assert param_4 == -2
    obj.pop()
    param_3 = obj.top()
    assert param_3 == -1
    param_4 = obj.getMin()
    assert param_4 == -2
    obj.pop()
    param_4 = obj.getMin()
    assert param_4 == -2
    obj.pop()



if __name__ == "__main__":
    test1()
    test2()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()