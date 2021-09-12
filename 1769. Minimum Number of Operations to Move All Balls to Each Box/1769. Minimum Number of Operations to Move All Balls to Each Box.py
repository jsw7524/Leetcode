from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left1=right1=minOp=0
        for i,digit in enumerate(boxes):
            if '1'==digit:
                minOp+=i
                right1+=1
        minOp +=right1
        result=[]
        for i,digit in enumerate(boxes):
            minOp=left1+minOp-right1      
            result.append(minOp)     
            if '1'==digit: 
                right1-=1
                left1+=1
        return result
    
sln=Solution()
assert [11,8,5,4,3,4]==sln.minOperations(boxes = "001011")
assert [1,1,3]==sln.minOperations(boxes = "110")                 
assert [447,427,409,391,373,357,341,327,313,301,289,279,269,259,249,239,231,225,221,219,217,215,215,215,215,217,221,227,235,245,255,265,277,291,307,325,345,367]==sln.minOperations(boxes = "11001010101000011110010011111001111110")  

