from typing import List

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, idx, l, r):
        if l == r:
            self.tree[idx] = arr[l]
        else:
            mid = (l + r) // 2
            self.build(arr, 2 * idx + 1, l, mid)
            self.build(arr, 2 * idx + 2, mid + 1, r)
            self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def update(self, i, val, l=0, r=None, idx=0):
        if r is None:
            r = self.n - 1
        if l == r:
            self.tree[idx] = val
            return
        mid = (l + r) // 2
        if i <= mid:
            self.update(i, val, l, mid, 2 * idx + 1)
        else:
            self.update(i, val, mid + 1, r, 2 * idx + 2)
        self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, ql, qr, l=0, r=None, idx=0):
        if qr < 0:
            return 0;
        if r is None:
            r = self.n - 1
        if ql <= l and qr >= r:
            return self.tree[idx]
        if qr < l or ql > r:
            return float('-inf')
        mid = (l + r) // 2
        left = self.query(ql, qr, l, mid, 2 * idx + 1)
        right = self.query(ql, qr, mid + 1, r, 2 * idx + 2)
        return max(left, right)


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        st=SegmentTree([0 for i in range(n+1)] )
        for start, end, price in sorted(offers):       
            previousMax=st.query(0,start-1)
            if previousMax + price > st.query(end, end): 
                st.update(end, previousMax + price)
        return st.query(0, n-1)
    
sln=Solution()
assert 13==sln.maximizeTheProfit(n = 4, offers = [[0,0,5],[3,3,1],[1,2,5],[0,0,7]])
assert 12==sln.maximizeTheProfit(n = 10, offers = [[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]])
assert 10==sln.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]])
assert 3==sln.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]])
