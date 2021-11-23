from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        lenTickets=len(tickets)
        times=(lenTickets)*(tickets[k]-1)
        for i in range(lenTickets):
            if (tickets[i]-(tickets[k]-1))  < 0:
                times+= (tickets[i]-(tickets[k]-1))

        for i in range(k+1):
            if (tickets[i]-(tickets[k]-1))  > 0:
                times+=1                
        return times

sln=Solution()


assert 585==sln.timeRequiredToBuy([88,76,77,82,62,20,26,72,45,54],2) 
assert 154==sln.timeRequiredToBuy([84,49,5,24,70,77,87,8],3) 
assert 8==sln.timeRequiredToBuy(tickets = [5,1,1,1], k = 0)    
assert 6==sln.timeRequiredToBuy(tickets = [2,3,2], k = 2)    
assert 5==sln.timeRequiredToBuy(tickets = [5], k = 0)   
