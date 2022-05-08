class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxValue=-1
        for i in range((len(num)-3)+1):
            if num[i] == num[i+1] == num[i+2]:
                maxValue=max(int(num[i:i+3]), maxValue)
        if maxValue==-1:
            return ""
        return  "000" if 0==maxValue else str(maxValue)
    
sln=Solution()

assert "222"==sln.largestGoodInteger( num = "222")
assert "777"==sln.largestGoodInteger(num = "6777133339")
assert "000"==sln.largestGoodInteger( num = "2300019")
assert ""==sln.largestGoodInteger( num = "42352338")
