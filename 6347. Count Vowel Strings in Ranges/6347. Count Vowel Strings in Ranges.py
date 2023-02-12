from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        vowels=['a', 'e', 'i', 'o','u']
        isValid=[0] * n
        prefixSum=[0] * n
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                isValid[i]=1
        prefixSum[0]=isValid[0]
        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+isValid[i]
        result=[]
        for l,r in queries:
            result.append(prefixSum[r]-prefixSum[l]+isValid[l])
        return result
    
sln=Solution()
assert [3,2,1]==sln.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
assert [2,3,0]==sln.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
            
            
        
                