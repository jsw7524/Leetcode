from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        #stage 1
        record = [ 0 for i in range(1+2*target)]
        coins.sort()
        record[coins[0]]=1
        for c in coins[1:]:
            for i in range(target, 0, -1):
                if 1==record[i]:
                    record[i+c]=1
            record[c]=1        
        #stage 2
        counter=0
        record[0]=1
        for c in range(1, target+1):
            if 0==record[c]:
                for i in range(target, 0, -1):
                    if 1==record[i]:
                        record[i+c]=1
                record[c]=1     
                counter+=1            
        return counter
    
sln=Solution()
assert 4==sln.minimumAddedCoins(coins = [15,1,12], target = 43)
assert 3==sln.minimumAddedCoins(coins = [1,1,1], target = 20)
assert 1==sln.minimumAddedCoins(coins = [1,4,10,5,7,19], target = 19)
assert 2==sln.minimumAddedCoins(coins = [1,4,10], target = 19)                    