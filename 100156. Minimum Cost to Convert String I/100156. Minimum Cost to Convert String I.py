from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(len(original)):
            dist[(ord(original[i])-97)][(ord(changed[i])-97)]=min(dist[(ord(original[i])-97)][(ord(changed[i])-97)],cost[i])
        for i in range(n):
            dist[i][i]=0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        minCost=0
        for i in range(len(source)):
            if float('inf')==dist[(ord(source[i])-97)][(ord(target[i])-97)]:
                return -1
            minCost+=dist[(ord(source[i])-97)][(ord(target[i])-97)]
        return int(minCost)
    
sln=Solution()
assert -1==sln.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000])
assert 12==sln.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
assert 28==sln.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
            
            