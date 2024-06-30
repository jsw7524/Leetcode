class Solution:
    def makeTriangle(self,a,b,depth):
        if a >= depth:
            return self.makeTriangle(b,a-depth,depth+1)
        return depth-1
        
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.makeTriangle(red,blue,1),self.makeTriangle(blue,red,1))
    
sln=Solution()
assert 1==sln.maxHeightOfTriangle( red = 1, blue = 1)
assert 2==sln.maxHeightOfTriangle( red = 10, blue = 1)
assert 2==sln.maxHeightOfTriangle(red = 2, blue = 1)
assert 3==sln.maxHeightOfTriangle(red = 2, blue = 4)
        