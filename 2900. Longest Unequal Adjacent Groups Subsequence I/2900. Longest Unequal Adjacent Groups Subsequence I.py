from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ls=[0]
        for i in range(1,n):
            if groups[i] != groups[ls[-1]]:
                ls.append(i)
        return [words[i] for i in ls]
                
                
sln=Solution()
assert ["a","b","c"]==sln.getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,0,1,1])
assert ["e","b"]==sln.getWordsInLongestSubsequence(n = 3, words = ["e","a","b"], groups = [0,0,1])
                
                