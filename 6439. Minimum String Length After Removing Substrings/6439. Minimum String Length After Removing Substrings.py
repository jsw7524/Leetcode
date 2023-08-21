class Solution:
    def minLength(self, s: str) -> int:
        while True:
            tmp=s
            s=s.replace("AB","")
            s=s.replace("CD","")
            if s==tmp:
                return len(tmp)
        return -1
    
sln=Solution()
assert 5==sln.minLength(s = "ACBBD")   
assert 2==sln.minLength(s = "ABFCACDB")            
                