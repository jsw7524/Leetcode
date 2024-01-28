class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        counter=0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                counter+=1
        return counter
    
sln=Solution()
assert 0==sln.countKeyChanges(s = "AaAaAaaA")
assert 2==sln.countKeyChanges(s = "aAbBcC")
                
            
        