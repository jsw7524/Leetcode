class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        num=12
        n=2
        while num < neededApples:
            n+=2
            num+=4*((n+1)*(n//2)+(1+n//2)*(n//2))-4*n
            #print(n,num)
        return 4*n

sln=Solution()
assert 8==sln.minimumPerimeter(neededApples = 1)    
assert 16==sln.minimumPerimeter(neededApples = 13)    
assert 5040==sln.minimumPerimeter(neededApples = 1000000000)           
    
            