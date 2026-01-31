
class MyStack:
    def __str__(self):
        result="stack:\n"
        for elm in self.data[::-1]:
            result+=str(elm)+" "
        return result

    def __init__(self):
        self.data=[]        
        self.length=0

    def push(self, val) -> None:       
        self.data.append(val)            
        self.length+=1

    def pop(self):
        if self.length==0:
            return None
        self.length-=1    
        return self.data.pop(-1)  

    def top(self):
        return self.data[-1]
        
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = MyStack()
        for elm in path.split("/"):
                      
            if elm == "..":
                stack.pop()
            elif elm == "." or elm == "" :
                pass
            else:
                stack.push(elm)
        #print(stack) 
        return "/" + "/".join(stack.data)


if __name__ == "__main__":
    sol = Solution()
    assert "/c" == (sol.simplifyPath("/a/./b/../../c/"))  # Output: "/c"
    assert "/" == (sol.simplifyPath("/../"))  # Output: "/"
    assert "/home/foo" == (sol.simplifyPath("/home//foo/"))  # Output: "/home/foo"