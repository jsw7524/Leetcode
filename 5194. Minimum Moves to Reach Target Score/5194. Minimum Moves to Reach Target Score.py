class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        current=target
        times=0
        while maxDoubles > 0 and current != 1:
            if current%2==1:
                current-=1
                times+=1
            current//=2
            times+=1
            maxDoubles-=1
        return times + current -1

sln=Solution()
assert 4==sln.minMoves(target = 10, maxDoubles = 4)        
assert 4==sln.minMoves(target = 5, maxDoubles = 0)
assert 7==sln.minMoves(target = 19, maxDoubles = 2)
            
