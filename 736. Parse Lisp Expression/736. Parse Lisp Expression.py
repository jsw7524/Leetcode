import re

class Token:
    def __init__(self, typeName , content) -> None:
        self.TypeName=typeName
        self.Content=content

class Tokenizer:
    def getTokens(self, expression):
        pattern="(?P<let>let)|(?P<mult>mult)|(?P<add>add)|(?P<lp>\()|(?P<rp>\))|(?P<int>-?\d+)|(?P<var>[a-z]\w*)"
        regex = re.compile(pattern)
        matches = regex.finditer(expression)
        result=[]
        for m in matches:
            result.append(Token(m.lastgroup,m[0]))
        return result

class AddExpression:
    def __init__(self,e1,e2) -> None:
        self.e1=e1
        self.e2=e2
        self.value=0
    
    def evaluate(self):
        self.value=self.e1.evaluate()+self.e2.evaluate()
        return self.value

class MultExpression:
    def __init__(self,e1,e2) -> None:
        self.e1=e1
        self.e2=e2
        self.value=0
    
    def evaluate(self):
        self.value=self.e1.evaluate()*self.e2.evaluate()
        return self.value

class ConstNumberExpression:
    def __init__(self, value) -> None:
        self.value=value
    def evaluate(self):
        return self.value
    
class VariableExpression:
    def __init__(self, name) -> None:
        self.name=name
        self.value=0
    def setValue(self, value):
        self.value=value      
    def evaluate(self):
        return self.value
    
class LetExpression:
    def __init__(self, variables_subExpressions, expr) -> None:
        self.variables_subExpressions=variables_subExpressions
        self.expression=expr
        self.Value=0
    
    def evaluate(self):
        for var,expr in self.variables_subExpressions:
            var.setValue(expr.evaluate())
        return self.expression.evaluate()

class Parser:
    def parse(self, tokens, index):
        for t in tokens:
        

class Solution:
    def evaluate(self, expression: str) -> int:
        tokens=tokenizer.getTokens(expression)
        
        
##########################################################################    
tokenizer=Tokenizer()
assert 18==len(tokenizer.getTokens(expression = "(let x 1 y 2 x (add x y) (add x y))"))
assert 21==len(tokenizer.getTokens(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"))
assert 8==len(tokenizer.getTokens(expression = "(let x 3 x 2 x)"))
##########################################################################   
constNumber1 = ConstNumberExpression(1)
assert 1 == constNumber1.evaluate()
##########################################################################   
constNumber2 = ConstNumberExpression(2)
constNumber3 = ConstNumberExpression(3)
addExpression=AddExpression(constNumber2,constNumber3)
assert 5 == addExpression.evaluate()
##########################################################################   
multExpression=MultExpression(constNumber2,constNumber3)
assert 6 == multExpression.evaluate()
##########################################################################   
testExpression= MultExpression(AddExpression(constNumber1,constNumber3),constNumber2)
assert 8 == testExpression.evaluate()
##########################################################################   
variableX = VariableExpression("x")
letExpression = LetExpression([(variableX,constNumber3), (variableX,constNumber2)],variableX,[])
assert 2==letExpression.evaluate()
##########################################################################   
variableX = VariableExpression("x")
testExpression= MultExpression(AddExpression(constNumber1,constNumber3),constNumber2)
letExpression = LetExpression([(variableX,constNumber1),(variableX,constNumber2), (variableX,testExpression)],variableX,[])
assert 8==letExpression.evaluate()