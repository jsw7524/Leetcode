from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes=[[0,0,0]]
        for b ,p in brackets:
            if b > income:
                b=income
            pb=taxes[-1][0]
            taxes.append((b,p,b-pb))
            if b==income:
                break
        answer= sum([r*(p/100) for b,p,r in taxes])
        return answer

sln=Solution()
assert 0.00000==sln.calculateTax(brackets = [[2,50]], income = 0)
assert 0.25000==sln.calculateTax(brackets = [[1,0],[4,25],[5,50]], income = 2)
assert 2.65000==sln.calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10)
            
        