class Solution:
    def GetOnes(self, x):
        return bin(x).count("1")
    def OnesToZeros(self, binstr, n):
        tmp=list()
        for c in binstr:
            if c == "1":
                if n>0:
                    tmp.append("1")
                    n-=1
                else:
                    tmp.append("0")
            else:
                tmp.append("0")                
        return  ''.join(tmp)

    def ZerosToOnes(self, binstr, n):
        tmp=list()
        
        for c in binstr[::-1]:
            if c == "0":
                if n>0:
                    tmp.append("1")
                    n-=1
                else:
                    tmp.append("0")
            else:
                tmp.append("1")
        for i in range(n):
            tmp.append("1")
        return  ''.join(tmp[::-1])
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        oneNum1=self.GetOnes(num1)
        oneNum2=self.GetOnes(num2)
        if oneNum1 >= oneNum2:
            return int(self.OnesToZeros(bin(num1).replace("0b",""),oneNum2),2)
        else:
            return int(self.ZerosToOnes(bin(num1).replace("0b",""),oneNum2-oneNum1),2)
        
sln=Solution()

assert 67==sln.minimizeXor(num1 = 65, num2 = 84)  

assert 3==sln.minimizeXor(num1 = 1, num2 = 12)        
assert 3==sln.minimizeXor(num1 = 3, num2 = 5)          
                    
                    