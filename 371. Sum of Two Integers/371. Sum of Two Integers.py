class Solution:
    def halfAdder(self, a, b):
        return  ( a^b, a & b)
    def fullAdder(self, a, b, cin):
        stmp1, ctmp1 = self.halfAdder(a, b)
        s, ctmp2 = self.halfAdder(stmp1, cin)
        return (s, ctmp1 | ctmp2)
    def Add(self, a, b):
        result: int=0
        c: int = 0
        for i in range(32):
            ai, bi = a%2, b%2
            s, c = self.fullAdder(ai, bi,c)
            a , b = a//2, b//2
            result+= s << i
        return result       
    def getSum(self, a: int, b: int) -> int:
        answer: int=self.Add(a, b)
        return answer
        #return -(2**32-answer) if answer > 2**31-1 else answer
      
sln=Solution()
assert -203==sln.getSum(-101,-102)
assert -3==sln.getSum(-1,-2)
assert 3==sln.getSum(1,2)
assert 35==sln.getSum(11,24)
assert 975==sln.getSum(151,824)