from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0,0)
        opTime=0
        for i,g in zip(range(len(garbage)-1,-1,-1), garbage[::-1]):
            if 'M' in g:
                opTime+=sum(travel[:i+1])
                break
                
        for i,g in zip(range(len(garbage)-1,-1,-1), garbage[::-1]):
            if 'G' in g:
                opTime+=sum(travel[:i+1])   
                break
            
        for i,g in zip(range(len(garbage)-1,-1,-1), garbage[::-1]):
            if 'P' in g:
                opTime+=sum(travel[:i+1])
                break
                
        return len(''.join(garbage)) + opTime   
    
sln=Solution()
assert 37==sln.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])        
assert 21==sln.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3])        
                
        
        