
class DisjointSet(object):
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.kinds=n

    def FindRoot(self,x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.FindRoot(self.parent[x])
            return self.parent[x]

    def Union_Sets(self,x,y):
        root1=self.FindRoot(x)
        root2=self.FindRoot(y)

        if root1 > root2:
            root1, root2 = root2, root1 

        if root1 == root2:
            return

        self.kinds-=1
        if self.size[root1] >= self.size[root2]:
            self.parent[root2]=root1
            self.size[root1]+=self.size[root2]
        else:
            self.parent[root1]=root2
            self.size[root2]+=self.size[root1]

    def Same_Set(self,x,y):
        return self.FindRoot(x)==self.FindRoot(y)

if __name__ == "__main__":
    ds=DisjointSet(10)
    for i in range(0,7,2):
        ds.Union_Sets(i,i+2)
    assert 6==ds.kinds
    assert 0==ds.FindRoot(6)
    assert True==ds.Same_Set(2,8)
    assert False==ds.Same_Set(1,8)