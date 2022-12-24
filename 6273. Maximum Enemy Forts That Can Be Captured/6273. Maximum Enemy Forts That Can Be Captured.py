class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        n = len(forts)
        count=0
        maxCount=0
        for i in range(n):
            if forts[i]==1 or forts[i]==-1:
                for j in range(i+1,n):
                    if forts[j] == 0:
                        count+=1
                    elif forts[j] == forts[i]:
                        count=0
                        break
                    elif forts[j] == -forts[i]:
                        maxCount=max(maxCount, count)
                        count=0
                        break
        return maxCount
    
sln=Solution()
assert 2==sln.captureForts(forts = [1,0,0,-1,0,0,-1,0,0,1])   
assert 4==sln.captureForts(forts = [1,0,0,-1,0,0,0,0,1])   
assert 0==sln.captureForts(forts = [-1,-1,1,-1,-1,0])  
assert 0==sln.captureForts(forts = [0,0,1,-1])                    
                
                
                
                