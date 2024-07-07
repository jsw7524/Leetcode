class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return ''.join(s[(i+k)%len(s)] for i in range(len(s)))
    
sln=Solution()
assert "aaa"==sln.getEncryptedString(s = "aaa", k = 1)
assert "tdar"==sln.getEncryptedString(s = "dart", k = 3)