import math
class SparseTableRMQ(object):
    def __init__(self, data) -> None:
        lenData=len(data)
        logLenData=math.ceil(math.log(lenData))+1
        self.table=[[0 for x in range(logLenData)] for y in range(lenData)]
        for i in range(lenData):
            self.table[i][0]=data[i]
        for j in range(1,logLenData):    
            for i in range(lenData):
                if (i+2**(j-1)) >= lenData:
                    self.table[i][j]=self.table[i][j-1]
                    continue
                if self.table[i][j-1] < self.table[i+2**(j-1)][j-1]:
                    self.table[i][j]=self.table[i][j-1]
                else:
                    self.table[i][j]=self.table[i+2**(j-1)][j-1]
        return

    def Query(self, left, right):
        if left==right:
            return self.table[left][0]
        distance=right-left
        distanceLog=math.ceil(math.log(distance))
        return min(self.table[left][distanceLog],self.table[right-(2**distanceLog)+1][distanceLog])

stRMQ=SparseTableRMQ(data=[i for i in range(1000)])
assert 0==stRMQ.Query(0,999)
assert 65==stRMQ.Query(65,848)
assert 123==stRMQ.Query(123,456)
assert 100==stRMQ.Query(100,100)

stRMQ=SparseTableRMQ(data=[7, 2, 3, 0, 5, 10, 3, 12, 18])
assert 2==stRMQ.Query(0,2)
assert 3==stRMQ.Query(4,7)
assert 12==stRMQ.Query(7,8)
assert 0==stRMQ.Query(0,9)
assert 10==stRMQ.Query(5,5)
