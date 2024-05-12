class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sLen=len(s)
        info = { s[i]:i for i in range(sLen)}
        tLne=len(t)
        distance=0
        for i, ch in enumerate(t):
            distance+=abs(i-info[ch])
        return distance
    
sln=Solution()
assert 12==sln.findPermutationDifference(s = "abcde", t = "edbac")
assert 2==sln.findPermutationDifference(s = "abc", t = "bac")