class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, blank = 0, 0, 0
        for m in moves:
            if m == 'L':
                left+=1
            elif m == 'R':
                right+=1
            else:
                blank+=1
        return max(abs(-left + right + blank ), abs(-left + right - blank ))
    
sln=Solution()
assert 3==sln.furthestDistanceFromOrigin(moves = "L_RL__R")   
assert 5==sln.furthestDistanceFromOrigin(moves = "_R__LL_")                                
assert 7==sln.furthestDistanceFromOrigin(moves = "_______")                         