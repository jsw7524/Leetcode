from typing import List

class Solution:
    
    def flush(self):
        return sum([self.suits[s] >=5 for s in self.suits]) >=1
    def threeofaKind(self):
        return sum([self.ranks[r] >=3 for r in self.ranks]) >=1
    def pair(self):
        return sum([self.ranks[r] >=2 for r in self.ranks]) >=1
        
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        self.ranks={}
        for r in ranks:
            if r not in self.ranks:
                self.ranks[r]=0
            self.ranks[r]+=1
        self.suits={}
        for s in suits:
            if s not in self.suits:
                self.suits[s]=0
            self.suits[s]+=1
        if self.flush():
            return "Flush"
        if self.threeofaKind():
            return "Three of a Kind"
        if self.pair():
            return "Pair"
        return "High Card"
            