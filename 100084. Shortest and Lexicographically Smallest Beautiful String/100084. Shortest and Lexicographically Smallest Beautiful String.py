class Solution:
    
    def strMin(self, a ,b):
        la=len(a)
        lb=len(b)
        if la < lb:
            return a
        elif la > lb:
            return b
        else:
            return  b if  a > b else a
    
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        sLen=len(s)
        counter1=1 if s[0]=='1' else 0
        i, j = 0, 0
        bs="1"*101
        while i < sLen:
            if counter1==k:
                bs = self.strMin(s[i:j+1], bs)
                if s[i]=='1':
                    counter1-=1     
                i+=1
            elif counter1< k:
                if j < sLen-1:
                    j+=1
                    if s[j]=='1':
                        counter1+=1
                else:
                    break 
        return "" if bs == "1"*101 else bs

sln=Solution()
assert "1011"==sln.shortestBeautifulSubstring(s = "110101000010110101", k = 3)
assert "11111111001000101"==sln.shortestBeautifulSubstring(s = "111111110010001010", k = 11)
assert ""==sln.shortestBeautifulSubstring(s = "000", k = 1)
assert "11"==sln.shortestBeautifulSubstring(s = "1011", k = 2)
assert "11001"==sln.shortestBeautifulSubstring(s = "100011001", k = 3)
            