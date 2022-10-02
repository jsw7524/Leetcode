class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        states="abcdefghijklmnopqrstuvwxyz$"
        maxLength=0
        lenS=len(s)
        for i, c in enumerate(s):
            counter=0
            index=states.find(c)
            for j in range(i,min(i+26,lenS)):
                if s[j] == states[index]:
                    index+=1
                    counter+=1
                else:
                    break
            maxLength=max(maxLength, counter)
        return maxLength
    
sln=Solution()
assert 5==sln.longestContinuousSubstring(s = "zzzzzzzhijklzzzzzzzzz")
assert 1==sln.longestContinuousSubstring(s = "z")
assert 5==sln.longestContinuousSubstring(s = "abcde")
assert 2==sln.longestContinuousSubstring(s = "abacaba")
            
                    
            