class Solution:
    def minimumSteps(self, s: str) -> int:
        n1=s.count('1')
        slen=len(s)
        ms=0
        for i, c in enumerate(s):
            if c == '1':
                ms+=((slen-n1)-i)
                n1-=1
        return ms
    
sln=Solution()
assert 0==sln.minimumSteps( s = "0")
assert 0==sln.minimumSteps( s = "1")
assert 0==sln.minimumSteps( s = "0111")
assert 2==sln.minimumSteps( s = "100")
assert 1==sln.minimumSteps( s = "101")
                
                