class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        n0, n1 = 0, 0
        diff = 0
        for d in s:
            if d=='0':
                n0+=1
            else:
                n1+=1
        n=len(s)
        #0->1
        for i in range(n):
            if s[i]!=target[i]:
                diff+=1
                if s[i]=='0':
                    if n1 == 0:
                        return False
                    n0-=1
                    n1+=1
                    diff-=1
        #1->0
        for i in range(n):
            if s[i]!=target[i]:
                if s[i]=='1':
                    if n1 <= 1 :
                        return False
                    n0+=1
                    n1-=1
                    diff-=1            
        
        if diff == 0:
            return True
        return False

sln=Solution()

assert False==sln.makeStringsEqual(s = "11", target = "00")   

assert True==sln.makeStringsEqual(s = "1010", target = "0110")          
                
        