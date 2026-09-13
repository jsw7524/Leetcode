class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        record = {}
        for index, number in enumerate(nums):
            if nums[index] not in record:
                record[nums[index]] = []
            record[nums[index]].append(index)
        # find numbers
        counter=0
        for n, loc in record.items():
            if  len(loc) == 3 and (loc[1]-loc[0] == loc[2]-loc[1]):
                counter+=1
        return counter

sln=Solution()
assert 2 == sln.countSpecialIntegers([1,8,1,5,1,5,8,5])
assert 0 == sln.countSpecialIntegers([8,8,8,8])
assert 0 == sln.countSpecialIntegers([8,6,6,8,8])

