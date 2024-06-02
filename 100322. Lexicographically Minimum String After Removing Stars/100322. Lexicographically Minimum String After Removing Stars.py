import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        result=[]
        tmp=list(s)
        for i,ch in enumerate(tmp):
            if ch=='*':
                loc, w= heapq.heappop(result)
                tmp[-loc]='@'
            else:
                heapq.heappush(result,(-1*(100000*ord(ch)+i),ch))
        return ''.join([ c for c in tmp if c !='@' or c!='*'])

sln=Solution()
assert "aab"==sln.clearStars( s = "aaba*")
            
                
                