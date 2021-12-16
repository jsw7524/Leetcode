class Solution:
    def countPoints(self, rings: str) -> int:
        lenRings=len(rings)
        rgb=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0,lenRings,2):
            color=rings[i]
            position=int(rings[i+1])
            if color=='R':
                rgb[position][0]+=1
            elif color=='G':
                rgb[position][1]+=1            
            elif color=='B':
                rgb[position][2]+=1
        answer=[ 1 if r[0]>0 and r[1]>0 and r[2]>0 else 0 for r in rgb]
        return sum(answer)

sln=Solution()
assert 1==sln.countPoints(rings = "B0B6G0R6R0R6G9")
assert 1==sln.countPoints(rings = "B0R0G0R9R0B0G0")
assert 0==sln.countPoints(rings = "G4")         
