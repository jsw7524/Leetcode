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
    # LL Parser cannot use left recursion Grammar
    # Grammar:
    # S -> LET | MUL | ADD
    # LET -> ( let VE EXPR )
    # VE -> VAR EXPR VE | EMPTY
    # EXPR -> VAR | NUM | LET | MUL | ADD
    # MUL -> ( mul EXPR EXPR )
    # ADD -> ( add EXPR EXPR )
    def parse(self, s):
        tokens=tokenizer.getTokens(s)
        return self.LET(tokens,0)

    def LET(self, tokens, position):
        if self.LP( tokens, position): 
            if "let"==tokens[position+1].TypeName:
                s1=self.VE( tokens, position+2)
                if s1>=0:
                    s2=self.EXPR(tokens, position +2 + s1)
                    if s2 >=1:
                        if self.RP( tokens, position+2+ s1+s2)==1:
                            return 2+ s1+s2+1
        return 0
    
    def MUL(self, tokens, position):
        if self.LP( tokens, position): 
            if "mult"==tokens[position+1].TypeName:
                s1=self.EXPR( tokens, position+2)
                if s1 >=1:
                    s2=self.EXPR( tokens, position+2+s1)
                    if s2 >= 1:
                        if self.RP( tokens, position+2+ s1+s2) ==1:
                            return  2+ s1+s2+1
        return 0      
      
    def ADD(self, tokens, position):
        if self.LP( tokens, position): 
            if "add"==tokens[position+1].TypeName:
                s1=self.EXPR( tokens, position+2)
                if s1 >=1:
                    s2=self.EXPR( tokens, position+2+s1)
                    if s2 >= 1:
                        if self.RP( tokens, position+2+ s1+s2) ==1:
                            return  2+ s1+s2+1
        return 0 
                             
    def EXPR(self, tokens, position):
        if self.VAR(tokens, position):
            return 1
        if self.NUM(tokens, position):
            return 1
        s1=self.LET(tokens, position)
        if s1>0:
            return s1
        s2=self.MUL(tokens, position)
        if s2 >0:
            return s2       
        s3=self.ADD(tokens, position)
        if s3 >0:
            return s3
        return 0       
                
    def VE(self, tokens, position):
        if 1==self.VAR(tokens, position):
            s1=self.EXPR( tokens, position + 1) 
            if s1 >= 1:
                s2=self.VE( tokens, position +1 + s1)
                if s2 >=0:
                    return  1 + s1 + s2
        return 0   
   
    def NUM(self, tokens, position):
        if "int" == tokens[position].TypeName:
            return 1
        return 0
 
    def VAR(self, tokens, position):
        if "var" == tokens[position].TypeName:
            return 1
        return 0       

    def LP(self, tokens, position):
        if "lp" == tokens[position].TypeName:
            return 1
        return 0 
    
    def RP(self, tokens, position):
        if "rp" == tokens[position].TypeName:
            return 1
        return 0     

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
# variableX = VariableExpression("x")
# letExpression = LetExpression([(variableX,constNumber3), (variableX,constNumber2)],variableX,[])
# assert 2==letExpression.evaluate()
##########################################################################   
# variableX = VariableExpression("x")
# testExpression= MultExpression(AddExpression(constNumber1,constNumber3),constNumber2)
# letExpression = LetExpression([(variableX,constNumber1),(variableX,constNumber2), (variableX,testExpression)],variableX,[])
# assert 8==letExpression.evaluate()
########################################################
parser=Parser()

parser.parse("(let x 2 (mult x (let x 3 y 4 (add x y))))")

# parser.parse("(let x 1 y 2 x (add x y) (add x y))")
# parser.parse("(let x 3 x 2 x)")