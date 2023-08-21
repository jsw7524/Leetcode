from typing import List

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

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        buckets=[ 0 for i in range(101)]
        ft=FenwickTree(101)
        result=[]
        n=len(nums)
        for i in range(k):
            buckets[nums[i]+50]+=1
            ft.update(nums[i]+51, 1)
                 
        beautyIndex = ft.find_closest_prefix_sum(x)
        if beautyIndex < 51:
            result.append(beautyIndex-51)
        else:
            result.append(0)
        
        for i in range(1, n - k + 1):
            buckets[nums[i-1]+50]-=1
            ft.update(nums[i-1]+51, -1)
            buckets[nums[i+k-1]+50]+=1
            ft.update(nums[i+k-1]+51, 1)
            beautyIndex = ft.find_closest_prefix_sum(x)
            if beautyIndex < 51:
                result.append(beautyIndex-51)
            else:
                result.append(0)
        return result
    
sln=Solution()
assert [0]==sln.getSubarrayBeauty(nums = [-50,14], k = 2, x = 2)               
assert [-3,0,-3,-3,-3]==sln.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1)  
assert [-1,-2,-3,-4]==sln.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2)               
assert [-1,-2,-2]==sln.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2)               
        
            