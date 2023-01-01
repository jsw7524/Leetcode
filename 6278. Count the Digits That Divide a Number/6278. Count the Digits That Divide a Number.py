class Solution:
    def countDigits(self, num: int) -> int:
        answer=0
        for n in str(num):
            d=int(n)
            if d > 0:
                if num%d==0:
                    answer+=1
        return answer
    
sln=Solution()
assert 4==sln.countDigits(num = 1248)
assert 2==sln.countDigits(num = 121)
assert 1==sln.countDigits(num = 7)
                
                