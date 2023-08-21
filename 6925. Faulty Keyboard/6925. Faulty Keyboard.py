class Solution:
    def finalString(self, s: str) -> str:
        result=[]
        for c in s:
            if c != 'i':
                result.append(c)
            else:
                result.reverse()
        return ''.join(result)

sln=Solution()
assert "ponter"==sln.finalString(s = "poiinter")
assert "rtsng"==sln.finalString(s = "string")
                
                