class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                num_zeros = substring.count('0')
                num_ones = substring.count('1')
                if num_zeros <= k or num_ones <= k:
                    count += 1
        return count
    
sln=Solution()
assert 15==sln.countKConstraintSubstrings(s = "11111", k = 1)
assert 25==sln.countKConstraintSubstrings(s = "1010101", k = 2)
assert 12==sln.countKConstraintSubstrings(s = "10101", k = 1)