from typing import List

class Solution:
    def smallestNumber(self, num: int) -> int:
        digits=list(str(num))
        if num == 0:
            return 0
        elif num > 0:
            digits.sort()
            if digits[0] == '0':
                for i,d in enumerate(digits):
                    if d != '0':
                        digits[0],digits[i] = digits[i],digits[0]
                        break            
            return int("".join(digits))
        else:
            return int('-'+''.join(sorted(digits[1:],reverse=True)))
        
sln=Solution()
assert 103==sln.smallestNumber(num = 310)
assert -7650==sln.smallestNumber(num = -7605)