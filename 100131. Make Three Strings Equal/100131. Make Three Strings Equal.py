class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i=0         
        if s1[i] != s2[i] or s2[i] != s3[i]:
            return -1
        while i < (min(len(s1),len(s2),len(s3))):
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break
            i+=1
        return  len(s1)-i + len(s2) - i + len(s3) - i

sln=Solution()
assert 0==sln.findMinimumOperations( s1 = "a", s2 = "a", s3 = "a")
assert -1==sln.findMinimumOperations( s1 = "dac", s2 = "bac", s3 = "cac")
assert 2==sln.findMinimumOperations(s1 = "abc", s2 = "abb", s3 = "ab")