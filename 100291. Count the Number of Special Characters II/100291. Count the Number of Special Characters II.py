class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        record={}
        result=0
        for i, ch in enumerate(word):
            if ch.isupper():
                if ch not in record:
                    record[ch]=i
            else:
                record[ch]=i
                
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in record and c.upper() in record:
                if record[c] < record[c.upper()]:
                    result+=1
        return result

sln=Solution()
assert 0==sln.numberOfSpecialChars(word = "abBCab")
assert 0==sln.numberOfSpecialChars(word = "abc")
assert 3==sln.numberOfSpecialChars(word = "aaAbcBC")
                