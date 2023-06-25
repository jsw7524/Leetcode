from typing import List

class FenwickTree:
    def __init__(self, n):
        sz = 1
        while sz <= n: sz <<= 1
        self.size = sz
        self.data = [0]*sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution:
    def matrixSumQueries(self, n, queries):
        row = [0]*n
        col = [0]*n
        row_time = FenwickTree(n)
        col_time = FenwickTree(n)
        row_val = FenwickTree(n)
        col_val = FenwickTree(n)
        time = 1
        for typei, indexi, vali in queries:
            if typei == 0:
                if row[indexi] != 0:
                    row_val.add(row_time.sum(indexi + 1), -row[indexi])
                row[indexi] = vali
                row_time.add(indexi + 1, time)
            else:
                if col[indexi] != 0:
                    col_val.add(col_time.sum(indexi + 1), -col[indexi])
                col[indexi] = vali
                col_time.add(indexi + 1, time)
            time += 1
        res = 0
        for i in range(n):
            if row[i] != 0:
                res += row[i] * (n - col_time.sum(row_time.sum(i + 1)))
            if col[i] != 0:
                res += col[i] * (n - row_time.sum(col_time.sum(i + 1)))
        return res
sln=Solution()
assert 17==sln.matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]])
assert 23==sln.matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]])