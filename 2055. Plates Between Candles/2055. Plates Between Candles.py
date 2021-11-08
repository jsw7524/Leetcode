from typing import List
import bisect

class Solution:
    
    def query(self, left, right):
        start=bisect.bisect_left(self.Candles, left)
        end=bisect.bisect_right(self.Candles, right)-1
        end=0 if end <=0 else end
        q=self.Candles[end]-self.Candles[start]-1 - (end-start-1)
        return 0 if q <= 0 else q
        
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        self.Candles=[]
        for i, c in enumerate(s):
            if c == '|':
                self.Candles.append(i)
        
        noCandles=False
        if len(self.Candles) == 0:
            noCandles = True    
                
        self.Candles.append(10**6)      
        result=[]
        for q in queries:
            if noCandles:
                result.append(0)
            else:
                result.append(self.query(q[0], q[1]))
        return result

sln=Solution()
assert [2, 3]==sln.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]])
assert [9,0,0,0,0]==sln.platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]])                   
assert [0]==sln.platesBetweenCandles(s = "||*", queries = [[2,2]])
assert [0]==sln.platesBetweenCandles(s = "***", queries = [[2,2]])
assert [0,1]==sln.platesBetweenCandles(s = "*|*|||", queries = [[0,0],[1,3]])