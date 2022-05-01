class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxValue=0
        for i,c in enumerate(number):
            if c==digit:
                maxValue=max(maxValue,int(number[:i]+number[i+1:]))
        return str(maxValue)
    
sln=Solution()
assert "12" == sln.removeDigit(number = "123", digit = "3")
assert "231" == sln.removeDigit(number = "1231", digit = "1")       
assert "51" == sln.removeDigit(number = "551", digit = "5") 