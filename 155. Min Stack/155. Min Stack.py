class MinStack:
    def __str__(self):
        result="stack\n"
        for elm in self.data[::-1]:
            result+=str(elm)+" "
        return result

    def __init__(self):
        self.min=[]
        self.data=[]        
        self.length=0

    def push(self, val: int) -> None:
        print("push")
        if self.length==0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1],val))               
        self.data.append(val)            
        self.length+=1
        print(self)

    def pop(self) -> None:
        print("pop")
        if self.length==0:
            return None
        self.length-=1    
        self.min.pop(-1)
        return self.data.pop(-1)  

    def top(self) -> int:
        print("top")
        return self.data[-1]
        

    def getMin(self):
        print("getMin")        
        if self.length == 0:
            return None
        return self.min[-1]
    

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
    #test1()
    test2()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()