
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        front =[  t if t<=tickets[k] else tickets[k] for t in tickets[:k]  ]
        rear = [  t if t<tickets[k] else tickets[k]-1  for t in tickets[k+1:] ]
        return sum(front)  + tickets[k] + sum(rear) 


if __name__ == "__main__":
    s = Solution()
    assert s.timeRequiredToBuy([2,3,2], 2) == 6
    assert s.timeRequiredToBuy([5,1,1,1], 0) == 8
    assert s.timeRequiredToBuy([84,49,5,24,70,77,87,8], 3) == 154
