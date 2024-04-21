class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        record={}
        result=0
        for ch in word:
            record[ch]=1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in record and c.upper() in record:
                result+=1
        return result
    
sln=Solution()
assert 1==sln.numberOfSpecialChars(word = "abBCab")
assert 0==sln.numberOfSpecialChars(word = "abc")
assert 3==sln.numberOfSpecialChars(word = "aaAbcBC")
                
            