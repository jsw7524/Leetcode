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