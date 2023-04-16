from typing import List

class Solution:      
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def largest_prime_on_diagonals(self, nums):
        n = len(nums)
        diagonals = set()
        for i in range(n):
            diagonals.add(nums[i][i])
            diagonals.add(nums[i][n-i-1])      
        largest_prime = 0
        for num in diagonals:
            if self.is_prime(num) and num > largest_prime:
                largest_prime = num    
        return largest_prime     
    
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        return self.largest_prime_on_diagonals(nums)
    
sln=Solution()
assert 17==sln.diagonalPrime(nums = [[1,2,3],[5,17,7],[9,11,10]])
assert 11==sln.diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]])