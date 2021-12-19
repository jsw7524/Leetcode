from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(8 * 10**5)
        result=[]
        k=0
        for i,c in enumerate(s):
            if i==spaces[k]:
                result.append(' ')
                k+=1
            result.append(s[i])
        return ''.join(result)
            
sln=Solution()
assert "Leetcode Helps Me Learn"==sln.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])
assert "i code in py thon"==sln.addSpaces(s = "icodeinpython", spaces = [1,5,7,9])
assert " s p a c i n g"==sln.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6])