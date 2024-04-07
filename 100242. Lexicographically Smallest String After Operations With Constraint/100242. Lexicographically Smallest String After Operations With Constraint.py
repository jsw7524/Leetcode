class Solution:
    

    def computeDistance(self, ch, k):
        pos=ord(ch)-ord('a')
        if 26-pos <= k or k-pos >= 0:
            minDis=999
            if 26-pos <= k:
                minDis = min(abs(26-pos), minDis)
            if k-pos >= 0:
                minDis = min(pos , minDis)
            return ('a',minDis)
        else:
            return (chr(ord('a')+pos-k),k)
            
    
    def getSmallestString(self, s: str, k: int) -> str:
        reuslt=[]
        for c in s:
            newStr, cost = self.computeDistance(c, k)
            reuslt.append(newStr)
            k-=cost
        return ''.join(reuslt)
    
sln=Solution()
assert  "lol"==sln.getSmallestString(s = "lol", k = 0)
assert  "aawcd"==sln.getSmallestString(s = "xaxcd", k = 4)
assert  "aaaz"==sln.getSmallestString(s = "zbbz", k = 3)
            
        