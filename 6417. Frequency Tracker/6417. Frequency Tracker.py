class FrequencyTracker:

    def __init__(self):
        self.times=[0] * (1+10**5)
        self.numbers=[0] * (1+10**5)        

    def add(self, number: int) -> None:
        old=self.numbers[number]
        self.numbers[number]+=1
        if old > 0:
            self.times[old]-=1
        self.times[old+1]+=1
        
    def deleteOne(self, number: int) -> None:
        old=self.numbers[number]
        if old > 0:
            self.numbers[number]-=1
            self.times[old]-=1
            self.times[old-1]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.times[frequency] > 0
        

