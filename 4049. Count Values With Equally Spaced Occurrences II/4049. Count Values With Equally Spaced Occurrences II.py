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
            if len(loc) >= 3:# and (loc[1]-loc[0] == loc[2]-loc[1]):
                for i in range(1, len(loc)):
                    if (loc[1]-loc[0] != loc[i]-loc[i-1]):
                        break
                else:
                    counter+=1
        return counter

sln=Solution()
assert 0==sln.countSpecialIntegers([8,6,6,8,8])
assert 2==sln.countSpecialIntegers([1,8,1,5,1,5,8,5])
assert 1==sln.countSpecialIntegers([8,8,8,8])

