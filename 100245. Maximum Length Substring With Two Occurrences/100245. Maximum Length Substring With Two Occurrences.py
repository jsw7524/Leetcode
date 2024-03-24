class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxLen=1
        record={}
        j=0
        n=len(s)
        for i in range(n):
            if s[i] not in record:
                record[s[i]]=0
            record[s[i]]+=1
            while record[s[i]] >= 3:
                record[s[j]]-=1
                j+=1
            maxLen=max(maxLen,i-j+1)
        return maxLen

sln=Solution()
assert 2==sln.maximumLengthSubstring(s = "aaaa")
assert 4==sln.maximumLengthSubstring(s = "bcbbbcba")
                
            
        