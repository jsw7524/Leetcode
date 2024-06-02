import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        result=[]
        tmp=list(s)
        for i,ch in enumerate(tmp):
            if ch=='*':
                loc, _= heapq.heappop(result)
                k=100000-loc%100000
                if k==100000:
                    k=0
                tmp[k]='@'
            else:
                heapq.heappush(result,((100000*ord(ch)+(100000-i)),ch))
        return ''.join(c for c in tmp if c !='@' and c!='*')

sln=Solution()
assert ""==sln.clearStars( s = "d*")
assert "abc"==sln.clearStars( s = "abc")
assert "aab"==sln.clearStars( s = "aaba*")
            
                
                