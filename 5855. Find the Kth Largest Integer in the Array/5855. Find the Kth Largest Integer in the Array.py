from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        data=[int(x) for x in nums]
        data.sort(reverse=True)
        return str(data[k-1])
    
sln=Solution()
assert "3"==sln.kthLargestNumber(nums = ["3","6","7","10"], k = 4)
assert "2"==sln.kthLargestNumber(nums = ["2","21","12","1"], k = 3)
assert "0"==sln.kthLargestNumber(nums = ["0","0"], k = 2)
        