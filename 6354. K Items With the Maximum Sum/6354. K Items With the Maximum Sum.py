class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        data=[1 for i in range(numOnes)] + [ 0 for i in range(numZeros)] + [ -1 for i in range(numNegOnes)]
        return sum(data[:k])
    
sln=Solution()
assert 3==sln.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4)
assert 2==sln.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2)