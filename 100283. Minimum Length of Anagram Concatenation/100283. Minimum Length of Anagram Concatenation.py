from collections import Counter
from math import gcd

def min_length_of_t(s):
    # Count the frequency of each character in s
    freq = Counter(s)
    
    # Get the length of s
    n = len(s)
    
    # Function to check if a given length can be the length of t
    def can_form_t(length):
        # For each character, check if its frequency is a multiple of the length
        for count in freq.values():
            if count % length != 0:
                return False
        return True
    
    # Check all divisors of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i is a divisor of n
            if can_form_t(i):
                return i
            # n // i is also a divisor of n
            if can_form_t(n // i):
                return n // i
    
    # If no divisor worked, return n (this line is technically unreachable)
    return n


class Solution:
    def minAnagramLength(self, s: str) -> int:
        return min_length_of_t(s)
        