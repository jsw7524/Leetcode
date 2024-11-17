class Solution:
    def isBalanced(self, num: str) -> bool:
        oddSum= sum(int(num[d]) for d in range(0,len(num),2))
        evenSum=sum(int(num[d]) for d in range(1,len(num),2))
        return oddSum == evenSum
    
sln=Solution()
assert True==sln.isBalanced(num = "24123")
#assert False==sln.isBalanced(num = "1234")