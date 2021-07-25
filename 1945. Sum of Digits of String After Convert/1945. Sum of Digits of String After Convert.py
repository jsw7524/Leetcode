class Solution:
    def Convert(self, s):
        tmp=[]
        for c in s:
            tmp.append(str(ord(c)-ord('a')+1))
        return ''.join(tmp)
    
    def Transform(self, s):
        tmp=0
        for c in s:
            tmp+=int(c)
        return str(tmp)
                    
    def getLucky(self, s: str, k: int) -> int:
        tmp=self.Convert(s)
        for i in range(k):
            tmp=self.Transform(tmp)
        return int(tmp)

sln=Solution()
assert 36==sln.getLucky(s = "iiii", k = 1)
assert 6==sln.getLucky(s = "leetcode", k = 2)
assert 8==sln.getLucky(s = "zbax", k = 2)


            
        