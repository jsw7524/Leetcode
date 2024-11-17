class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        for _ in range(9):
            word = word + "".join([ chr((ord(ch) - ord("a") +1)%26 + ord("a")) for ch in word])
        return word[k-1]
    
sln=Solution()
assert "c"==sln.kthCharacter(k = 10)
assert "b"==sln.kthCharacter(k = 5)
            