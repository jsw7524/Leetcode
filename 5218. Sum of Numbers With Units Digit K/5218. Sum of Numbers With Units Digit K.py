class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        if k==0:
            if num%10==0:
                return 1
            else:
                return -1
        i=1
        while num>=k*i:
            if num%10==(k*i)%10:
                return i
            i+=1
        return -1

sln=Solution()

assert -1==sln.minimumNumbers(num = 4, k = 0)

assert 0==sln.minimumNumbers(num = 0, k = 7)
assert -1==sln.minimumNumbers(num = 37, k = 2)
assert 2==sln.minimumNumbers(num = 58, k = 9)

