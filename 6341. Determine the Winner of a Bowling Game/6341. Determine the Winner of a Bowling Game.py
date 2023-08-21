from typing import List

class Solution:
    
    def scoring(self, player: List[int]):
        score = 0
        p1=0
        p2=0
        for i, s in enumerate(player):
            score+=(2 if p2==10 or p1==10 else 1)*s
            p2=p1  
            p1=s              
        return score

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1=self.scoring(player1)
        score2=self.scoring(player2)
        return 0 if score1==score2 else ( 1 if score1>score2 else 2)

sln=Solution()
assert 2==sln.isWinner([5,6,1,10],[5,1,10,5])
assert 1==sln.isWinner([9,7,10,7],[10,2,4,10])
assert 0==sln.isWinner(player1 = [2,3], player2 = [4,1])
assert 2==sln.isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2])
assert 1==sln.isWinner(player1 = [4,10,7,9], player2 = [6,5,2,3])