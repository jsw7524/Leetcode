class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] !='0':
                return  num[:i+1]
        return ''

sln=Solution()
assert "512301"==sln.removeTrailingZeros(num = "51230100")
assert "123"==sln.removeTrailingZeros(num = "123")
assert "1"==sln.removeTrailingZeros(num = "10")
assert "1"==sln.removeTrailingZeros(num = "1")
