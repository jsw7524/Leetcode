class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i=word.find(ch)
            return word[i::-1]+word[i+1:]
        return word
    
sln=Solution()
assert "dcbaefd"==sln.reversePrefix(word = "abcdefd", ch = "d")
assert "zxyxxe"==sln.reversePrefix(word = "xyxzxe", ch = "z")
assert "abcd"==sln.reversePrefix(word = "abcd", ch = "z")