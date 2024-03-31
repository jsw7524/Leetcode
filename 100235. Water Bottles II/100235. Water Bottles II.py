class Solution:
    def compute(self, numBottles, numExchange):
        if numBottles < numExchange:
            return 0
        else:
            return self.compute(numBottles-numExchange+1, numExchange+1) + 1
        
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        return self.compute(numBottles, numExchange)+numBottles
    
sln=Solution()
assert 13==sln.maxBottlesDrunk(numBottles = 10, numExchange = 3)
assert 15==sln.maxBottlesDrunk(numBottles = 13, numExchange = 6)
        