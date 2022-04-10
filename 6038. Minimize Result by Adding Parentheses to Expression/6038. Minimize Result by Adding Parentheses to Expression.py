class Solution:
    def minimizeResult(self, expression: str) -> str:
        leftPart, rightPart = expression.split("+")
        minValue=int(leftPart)+int(rightPart)
        answer=f"({leftPart}+{rightPart})"
        for i in range(0,len(leftPart)+1):
            for j in range(1,len(rightPart)+1):
                addLeft=leftPart[i:]
                mulLeft=leftPart[:i]  
                if addLeft == '':
                    addLeft='999999999'
                if mulLeft == '':
                    mulLeft='1'
                    
                addRight=rightPart[:j]
                mulRight=rightPart[j:]  
                if addRight == '':
                    addRight='999999999'
                if mulRight == '':
                    mulRight='1'

                if int(mulLeft)*(int(addLeft) + int(addRight))*int(mulRight) < minValue:
                    minValue=int(mulLeft)*(int(addLeft) + int(addRight))*int(mulRight)          
                    answer=f"{leftPart[:i]}({leftPart[i:]}+{rightPart[:j]}){rightPart[j:]}"
        return answer
    
sln=Solution()

sln.minimizeResult(expression = "5+22")

sln.minimizeResult(expression = "247+38")
sln.minimizeResult(expression = "1+2")
sln.minimizeResult(expression = "999+999")
sln.minimizeResult(expression = "12+34")
