class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter=0
        while not (num1 ==0  or num2 == 0):
            counter+=1
            if num1 >= num2:
                num1-=num2
            else:
                num2-=num1
        return counter
    
sln=Solution()
assert 3==sln.countOperations(num1=2,num2=3)
assert 1==sln.countOperations(num1 = 10, num2 = 10)