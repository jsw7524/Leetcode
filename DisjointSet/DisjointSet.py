
class DisjointSet(object):
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.groups=n

    def FindRoot(self,x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.FindRoot(self.parent[x])
            return self.parent[x]

    def UnionSets(self,x,y):
        root1=self.FindRoot(x)
        root2=self.FindRoot(y)

        if root1 > root2:
            root1, root2 = root2, root1 

        if root1 == root2:
            return

        self.groups-=1
        if self.size[root1] >= self.size[root2]:
            self.parent[root2]=root1
            self.size[root1]+=self.size[root2]
        else:
            self.parent[root1]=root2
            self.size[root2]+=self.size[root1]

    def SameSet(self,x,y):
        return self.FindRoot(x)==self.FindRoot(y)

    def GroupSize(self, x):
        return self.size[self.FindRoot(x)]

if __name__ == "__main__":
    ds=DisjointSet(10)
    for i in range(2,7,2):
        ds.UnionSets(i,i+2)
    ds.UnionSets(8,0)
    assert 6==ds.groups
    assert True==ds.SameSet(2,8)
    assert False==ds.SameSet(1,8)
    assert 5==ds.GroupSize(4)