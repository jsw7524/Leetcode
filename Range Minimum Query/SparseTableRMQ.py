import math
class SparseTableRMQ(object):
    def __init__(self, data, minimum=True) -> None:
        self.func= min if minimum else max
        n=len(data)
        logN=math.ceil(math.log2(n))+1
        self.table=[[data[i] for j in range(logN)] for i in range(n)]
        for j in range(1,logN):    
            for i in range(n):
                if (i+2**(j-1)) < n:
                    self.table[i][j]=self.func(self.table[i][j-1],self.table[i+2**(j-1)][j-1])
                else:
                    self.table[i][j]=self.table[i][j-1]    
        return

    def Query(self, left, right):
        if left==right:
            return self.table[left][0]
        distanceLog=math.floor(math.log2(right-left+1))
        return self.func(self.table[left][distanceLog],self.table[right-(2**distanceLog)+1][distanceLog])

stRMQ=SparseTableRMQ(data=[i for i in range(1000)],minimum=False)
assert 999==stRMQ.Query(0,999)
assert 848==stRMQ.Query(65,848)
assert 456==stRMQ.Query(123,456)
assert 100==stRMQ.Query(100,100)

stRMQ=SparseTableRMQ(data=[0,5,2,5,4,3,1,6,3],minimum=False)
assert 5==stRMQ.Query(3,4)
assert 3==stRMQ.Query(8,8)
assert 6==stRMQ.Query(1,8)
assert 6==stRMQ.Query(0,8)

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

stRMQ=SparseTableRMQ(data=[0,5,2,5,4,3,1,6,3])
assert 4==stRMQ.Query(3,4)
assert 3==stRMQ.Query(8,8)
assert 1==stRMQ.Query(1,8)
assert 0==stRMQ.Query(0,8)

import random
random.seed(7524)
test=[random.randint(-2**8,2**8) for i in range(999)]
stRMQ=SparseTableRMQ(test)
assert min(test[11:478+1])==stRMQ.Query(11,478)
assert min(test[210:397+1])==stRMQ.Query(210,397)
assert min(test[110:497+1])==stRMQ.Query(110,497)
assert min(test[0:999+1])==stRMQ.Query(0,999)

# sizeArray=9999
# sizeQuery=200
# random.seed(12345)
# test=[random.randint(-2**8,2**8) for i in range(sizeArray)]
# print(*test,file=open("test.txt","w"))
# print(sizeQuery,file=open("test.txt","a"))
# stRMQ=SparseTableRMQ(test)
# for p in range(sizeQuery):
#     l,r=random.randint(0,sizeArray//4),random.randint(sizeArray//4+sizeArray//2,sizeArray)
#     if l > r:
#         l,r=r,l
#     print(l,r,file=open("test.txt","a"))
#     print(stRMQ.Query(l,r),file=open("answer.txt","a"))
    