class Solution:
    def DFS(self, number: str, current: int, target: int):
        if number == "":
            if current == target:
                return True
        else:
            if current > target:
                return False
            if int(number)+current == target:
                return True
            for i in range(1,len(number)):       
                if True == self.DFS(number[i:], int(number[:i])+current, target):
                    return True
        return False
    
    def makeTable(self):
        pn=[]
        for i in range(1,1001):
            if self.DFS(str(i*i), 0, i):
                pn.append(i)
        return pn
                
    def punishmentNumber(self, n: int) -> int:
        pn=self.makeTable()
        #pn=[1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        return sum([p*p for p in pn if p <= n])
        
sln=Solution()
assert True==sln.DFS("1", 0, 1)
assert True==sln.DFS(str(1000*1000), 0, 1000)
assert True==sln.DFS(str(45*45), 0, 45)
assert 10804657==sln.punishmentNumber(n = 1000)
assert 3503==sln.punishmentNumber(n = 45)
assert 1==sln.punishmentNumber(n = 1)
assert 1478==sln.punishmentNumber(n = 37)
assert 182==sln.punishmentNumber(n = 10)
