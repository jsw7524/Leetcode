from typing import List
class Solution:
    def timeForType(self, garbageType, garbage, travel):
        for i,g in zip(range(len(garbage)-1,-1,-1), garbage[::-1]):
            if garbageType in g:
                return sum(travel[:i+1])
        return 0
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0,0)    
        return len(''.join(garbage)) + sum([self.timeForType(t ,garbage, travel) for t in "PGM" ])
    
sln=Solution()
assert 37==sln.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])        
assert 21==sln.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3])        
                
        
        