import re

class Solution:
    def Discounting(self, match):
        v=float(match[0][1:])
        tmp=v*((100-self.discount)/100) 
        return "$%.2f" %  tmp
    
    def discountPrices(self, sentence: str, discount: int) -> str:
        self.discount=discount
        result=[]
        for word in sentence.split(' '):
            result.append(re.sub(r"^\$[0-9]+(?:\.[0-9]+)?$",self.Discounting,word))
        return ' '.join(result)
    
sln=Solution()
assert "$2$3 $10.00 $100.00 $1.00 200 $33.00 33$ $$ $99.00 $99999.00 $9999999999.00"==sln.discountPrices("$2$3 $10 $100 $1 200 $33 33$ $$ $99 $99999 $9999999999", 0)
assert "ka3caz4837h6ada4 r1 $547.82"==sln.discountPrices(sentence = "ka3caz4837h6ada4 r1 $602", discount = 9)
assert "there are $0.50 $1.00 and 5$ candies in the shop"==sln.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50)
assert "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"==sln.discountPrices(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100)