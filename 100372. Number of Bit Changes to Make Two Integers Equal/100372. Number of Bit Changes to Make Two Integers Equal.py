class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Convert n and k to binary strings
        n_binary = bin(n)[2:]  # Remove the '0b' prefix
        k_binary = bin(k)[2:]

        max_length = max(len(n_binary), len(k_binary))
        n_binary = n_binary.zfill(max_length)
        k_binary = k_binary.zfill(max_length)

        changes = 0
        impossible = False

        for n_bit, k_bit in zip(reversed(n_binary), reversed(k_binary)):
            if n_bit == '1' and k_bit == '0':
                changes += 1
            elif n_bit == '0' and k_bit == '1':
                impossible = True
                break

        return -1 if impossible else changes

# Test cases
sln=Solution()
assert 2==sln.minChanges(13, 4)  # Expected output: 2
assert 0==sln.minChanges(21, 21)  # Expected output: 0
assert -1==sln.minChanges(14, 13)  # Expected output: -1