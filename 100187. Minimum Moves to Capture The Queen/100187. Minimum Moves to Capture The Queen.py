class Solution:
    def isWhiteBlock(self,x,y):
        return 1 if ((x%2)+y)%2 else 0

    def isBetweenVH(self,c1,mid,c2):
        if c1[0] == mid[0] == c2[0] and (c1[1] < mid[1] < c2[1] or c1[1] > mid[1] > c2[1]):
            return 1
        if c1[1] == mid[1] == c2[1] and (c1[0] < mid[0] < c2[0] or c1[0] > mid[0] > c2[0]):
            return 1   
        return 0     
    
    def isBetweenDiagonal(self,c1,mid,c2):
        if c1[0]-c1[1] == mid[0]-mid[1] == c2[0]-c2[1] and (c1[0] > mid[0] > c2[0] or c1[0] < mid[0] < c2[0] ) and (c1[1] > mid[1] > c2[1] or c1[1] < mid[1] < c2[1]):
            return 1
        if (9-c1[0]-c1[1]) == (9-mid[0]-mid[1]) == (9-c2[0]-c2[1]) and (c1[0] > mid[0] > c2[0] or c1[0] < mid[0] < c2[0] ) and (c1[1] > mid[1] > c2[1] or c1[1] < mid[1] < c2[1]):
            return 1   
        return 0    
        
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        result=[]
        # rook
        if a==e or b==f:
            result.append(1 + self.isBetweenVH((a,b),(c,d),(e,f)))
        else:
            result.append(2 + self.isBetweenVH((e,b),(c,d),(e,f)))
            result.append(2 + self.isBetweenVH((a,f),(c,d),(e,f)))
        # bishop
        if  self.isWhiteBlock(c,d) == self.isWhiteBlock(e,f):
            if c-d == e-f or ((9-c)-(d) == (9-e)-(f)):
                result.append(1+self.isBetweenDiagonal((c,d),(a,b),(e,f)))
        return min(result)
    
sln=Solution()
assert 1==sln.minMovesToCaptureTheQueen(a = 4, b = 3, c = 3, d = 4, e = 2, f = 5)
assert 2==sln.minMovesToCaptureTheQueen(a = 4, b = 3, c = 3, d = 4, e = 5, f = 2)
assert 2==sln.minMovesToCaptureTheQueen(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3)
assert 1==sln.minMovesToCaptureTheQueen(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2)
   