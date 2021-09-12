from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        info={}
        for width,height in rectangles:
            if width / height not in info:
                info[width / height]=0
            info[width / height]+=1
        result=0
        for r,n in info.items():
            result+=n*(n-1)/2
        return int(result)
        
sln=Solution()
assert 6==sln.interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]])
assert 0==sln.interchangeableRectangles(rectangles = [[4,5],[7,8]])        