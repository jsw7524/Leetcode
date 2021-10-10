class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result=0
        for i in range(low, high+1):
            si=str(i)
            length=len(si)
            if length%2==0:
                if sum([ int(c) for c in si[:length//2]]) == sum([ int(c) for c in si[length//2:]]):
                    result+=1
        return result
    
    
sln=Solution()
assert 4==sln.countSymmetricIntegers(low = 1200, high = 1230)  
assert 9==sln.countSymmetricIntegers(low = 1, high = 100)      
    
     
                