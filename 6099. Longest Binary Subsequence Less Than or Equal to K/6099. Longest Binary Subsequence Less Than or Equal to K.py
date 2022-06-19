class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        tmp=[s[0]]
        for ch in s[1:]:
            if int(''.join(tmp)+ch,base=2) > k:
                tmp.remove('1')
            tmp.append(ch)
        return len(tmp)

sln=Solution()
assert 6==sln.longestSubsequence(s = "00101001", k = 1)
assert 5==sln.longestSubsequence(s = "1001010", k = 5)

