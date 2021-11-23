from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] != colors[-1]:
            return len(colors)-1
        
        colorsLen=len(colors)
        i=0
        while i < colorsLen:
            if colors[i] != colors[-1]:
                break
            i+=1
        j=colorsLen-1
        while j >=0 :
            if colors[j] != colors[0]:
                break
            j-=1
            
        return max(j,(colorsLen-1)-i)
# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         colorsLen=len(colors)
#         maxLength=0
#         for i in range(colorsLen):
#             for j in range(i+1,colorsLen):
#                 if colors[i] != colors[j]:
#                     if abs(i-j) > maxLength:
#                         maxLength=abs(i-j)
#         return maxLength
    
sln=Solution()
assert 3==sln.maxDistance(colors = [1,1,1,6,1,1,1])                      
assert 4==sln.maxDistance(colors = [1,8,3,8,3])       
assert 1==sln.maxDistance(colors = [0,1]) 
assert 8==sln.maxDistance(colors = [4,4,4,11,4,4,11,4,4,4,4,4])           