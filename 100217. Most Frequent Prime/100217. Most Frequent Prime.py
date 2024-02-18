from typing import List
from collections import Counter
class Solution:


    def is_prime(self, n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_numbers(self, mat, start_row, start_col, direction, m, n):
        """Generate numbers in a given direction from a starting cell."""
        numbers = []
        current_number = ''
        row, col = start_row, start_col
        while 0 <= row < m and 0 <= col < n:
            current_number += str(mat[row][col])
            numbers.append(int(current_number))
            row += direction[0]
            col += direction[1]
        return numbers

    def most_frequent_prime(self, mat):
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        all_primes = []

        for i in range(m):
            for j in range(n):
                for direction in directions:
                    numbers = self.generate_numbers(mat, i, j, direction, m, n)
                    for number in numbers:
                        if number > 10 and self.is_prime(number):
                            all_primes.append(number)

        if not all_primes:
            return -1

        frequency = Counter(all_primes)
        most_common_primes = frequency.most_common()
        max_frequency = most_common_primes[0][1]
        max_primes = [prime for prime, freq in most_common_primes if freq == max_frequency]

        return max(max_primes) if max_primes else -1    
      
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        return self.most_frequent_prime(mat)
    
sln=Solution()
assert 97==sln.mostFrequentPrime(mat = [[9,7,8],[4,6,5],[2,8,6]])
assert -1==sln.mostFrequentPrime(mat = [[7]])
assert 19==sln.mostFrequentPrime(mat = [[1,1],[9,9],[1,1]])