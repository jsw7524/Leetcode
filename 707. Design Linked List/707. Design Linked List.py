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


def test1():
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    param_1 = obj.get(1)
    assert param_1 == 2
    obj.deleteAtIndex(1)
    param_2 = obj.get(1)
    assert param_2 == 3


if __name__ == "__main__":
    test1()