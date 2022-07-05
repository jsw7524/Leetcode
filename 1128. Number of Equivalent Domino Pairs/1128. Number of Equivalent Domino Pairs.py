from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs={}
        for d in dominoes:
            if d[0] > d[1]:
                d[0], d[1]=d[1], d[0]
            if (d[0], d[1]) not in pairs:
                pairs[(d[0], d[1])]=0
            pairs[(d[0], d[1])]+=1
        return sum([ p*(p-1)//2 for p in pairs.values() if p>1 ])
    
sln=Solution()
assert 1==sln.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]])
assert 3==sln.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]])
        
        
                
        