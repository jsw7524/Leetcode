class Solution:
    def partitionString(self, s: str) -> int:
        record={}
        subStrings=1
        for c in s:
            if c not in record:
                record[c]=0
            record[c]+=1
            if record[c]>=2:
                record.clear() 
                record[c]=1              
                subStrings+=1
        return subStrings

sln=Solution()

assert 6==sln.partitionString(s = "ssssss")
assert 4==sln.partitionString(s = "abacaba")
                
                