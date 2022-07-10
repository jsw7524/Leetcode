class SmallestInfiniteSet:

    def __init__(self):
        self.numberSet = set()
        self.upperBound = 1
        

    def popSmallest(self) -> int:
        tmp=0
        if len(self.numberSet)==0:
            tmp=self.upperBound
            self.upperBound+=1
            return tmp
        tmp=min(self.numberSet)
        self.numberSet.remove(tmp)
        return tmp
    
    def addBack(self, num: int) -> None:
        if num < self.upperBound:
            self.numberSet.add(num)
        
