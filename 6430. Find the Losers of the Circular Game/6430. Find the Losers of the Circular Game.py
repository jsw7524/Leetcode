from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friends={}
        friends[1]=True
        pos=1
        i=1
        while True:
            pos=(pos+i*k)%n
            if pos in friends:
                break
            else:
                friends[pos]=True
            i+=1         
        if 0 in friends:
            friends[n]=True  
        tmp=[ i for i in range(1,n+1) if i not in friends]
        return tmp
            
sln=Solution()

assert [2,3,4]==sln.circularGameLosers(n = 4, k = 4)
assert [4,5]==sln.circularGameLosers(n = 5, k = 2)