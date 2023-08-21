# Remenber the index of FenwickTree starts from 1
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def _lsb(self, i):
        return i & -i

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += self._lsb(index)

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= self._lsb(index)
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def find_closest_prefix_sum(self, target_sum):
        prefix_sum = 0
        index = 0
        bit_mask = 1 << (self.size.bit_length() - 1)

        while bit_mask > 0:
            next_index = index | bit_mask
            bit_mask >>= 1
            if next_index > self.size:
                continue

            if prefix_sum + self.tree[next_index] < target_sum:
                index = next_index
                prefix_sum += self.tree[next_index]

        if prefix_sum == target_sum:
            return index
        elif prefix_sum < target_sum and index < self.size:
            return index + 1
        else:
            return -1
