class Solution:
    def largestInteger(self, num: int) -> int:
        digits=list(str(num))
        odds=sorted([d for d in digits if int(d)%2==1],reverse=True)
        evens=sorted([d for d in digits if int(d)%2==0],reverse=True)
        result=[]
        for d in digits:
            if int(d)%2==1:
                result.append(odds.pop(0))
            else:
                result.append(evens.pop(0))
        return int(''.join(result))

sln=Solution()
assert 10==sln.largestInteger(num = 10)
assert 3412==sln.largestInteger(num = 1234)
assert 87655==sln.largestInteger(num = 65875)
assert 1==sln.largestInteger(num = 1)