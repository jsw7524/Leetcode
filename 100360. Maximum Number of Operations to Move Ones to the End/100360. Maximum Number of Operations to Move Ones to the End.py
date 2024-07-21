class Solution:
    def maxOperations(self, s: str) -> int:
        hasSpace=False
        number=s.lstrip("0")
        counter=0
        result=0
        for d in number:
            if d=='1':
                if hasSpace == True:
                    result+=counter
                    hasSpace=False
                counter+=1
            else:
                hasSpace=True
        if hasSpace == True:
            result+=counter
        return result
    
sln=Solution()

assert 2==sln.maxOperations(  s = "110")
assert 0==sln.maxOperations(  s = "00111")    
assert 4==sln.maxOperations( s = "1001101")               
                
                
            
            