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
    def isValid(self, s: str) -> bool:
        stack = MyStack()
        for char in s:
            if char in "({[":
                stack.push(char)
            elif char == ")":
                if stack.length == 0 or stack.pop() != "(":
                    return False
            elif char == "}":
                if stack.length == 0 or stack.pop() != "{":
                    return False
            elif char == "]":
                if stack.length == 0 or stack.pop() != "[":
                    return False
        return True if stack.length == 0 else False