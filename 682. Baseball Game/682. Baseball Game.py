
from typing import List

class MyStack:
    def __str__(self):
        result="stack\n"
        for elm in self.data[::-1]:
            result=str(elm)+" "
        return result

    def __init__(self):
        self.min=[]
        self.data=[]        
        self.length=0

    def push(self, val: int) -> None:
        if self.length==0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1],val))               
        self.data.append(val)            
        self.length+=1

    def pop(self) -> int:
        if self.length==0:
            return None
        self.length-=1    
        self.min.pop(-1)
        return self.data.pop(-1)  

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:       
        if self.length == 0:
            return None
        return self.min[-1]
    

class Solution:

    def check(self,s):
        """Checks if a string represents a valid integer or float, including negatives."""
        try:
            int(s)  # Try converting to a float (works for both int and float strings)
            return True
        except ValueError:
            return False


    def calPoints(self, operations: List[str]) -> int:
        stack=MyStack()
        for op in operations:
            if True == self.check(op):
                stack.push(int(op))
            elif "+"==op:
                v1=stack.pop()
                v2=stack.pop()
                stack.push(v2)
                stack.push(v1)               
                newScore=v1+v2
                stack.push(newScore)
            elif "D"==op:
                val=stack.top()
                stack.push(2*val)
            elif "C"==op:
                stack.pop()

        return sum(stack.data)



def test1():
    operations = ["5","2","C","D","+"]
    sol=Solution()
    result=sol.calPoints(operations)
    assert result == 30

def test2():
    operations = ["5","-2","4","C","D","9","+","+"]
    sol=Solution()
    result=sol.calPoints(operations)
    assert result == 27



if __name__ == "__main__":
    #test1()
    test2()
