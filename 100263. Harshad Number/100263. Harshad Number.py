
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digitSum = sum([int(c) for c in str(x) ])
        return digitSum if x % digitSum ==0 else -1

sln=Solution()
assert -1==sln.sumOfTheDigitsOfHarshadNumber(x=23)
assert 9==sln.sumOfTheDigitsOfHarshadNumber(x=18)

        