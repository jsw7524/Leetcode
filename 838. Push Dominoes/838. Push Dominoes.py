from collections import defaultdict

class FallingEvent:
    position:int
    direction:int
    def __init__(self, p, d) -> None:
        self.position=p
        self.direction=d

class Solution:
    
    def prepareQueue(self, arr:list[int])->list[FallingEvent]:
        eventQueue=[]
        for i, a in enumerate(arr):
            if a !=0:
                eventQueue.append(FallingEvent(i, a))
        return eventQueue
    
    def simulate(self, arr:list[int])->list[int]:
        eventQueue=self.prepareQueue(arr)
        updates=defaultdict(int)
        while len(eventQueue) > 0:
            updates.clear()
            while len(eventQueue) > 0:
                e = eventQueue.pop()
                if e.direction==1 and e.position+1<len(arr):
                    if arr[e.position+1]==0:
                        updates[e.position+1]+=1
                if e.direction==-1 and e.position-1>=0:
                    if arr[e.position-1]==0:
                        updates[e.position-1]-=1         
            for position in updates.keys():
                if updates[position]!=0:
                    arr[position]=updates[position]
                    eventQueue.append(FallingEvent(position,updates[position]))
        return arr
                    
    def pushDominoes(self, dominoes: str) -> str:
        arr=[]
        for d in dominoes:
            if d == '.':
                arr.append(0)
            elif d == 'L':
                arr.append(-1)
            elif d == 'R':
                arr.append(1)
        tmp=self.simulate(arr)
        return ''.join([ '.' if t == 0 else ('R' if t== 1 else 'L') for t in tmp])
    
sln=Solution()
assert "L"==sln.pushDominoes(dominoes = "L")
assert "RR.L"==sln.pushDominoes(dominoes = "RR.L")
assert "LL.RR.LLRRLL.."==sln.pushDominoes(dominoes = ".L.R...LR..L..")
    