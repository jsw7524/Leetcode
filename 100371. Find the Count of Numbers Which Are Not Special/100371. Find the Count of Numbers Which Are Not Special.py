class Solution:

    def sieve_of_eratosthenes(self, x):
        primes = [True] * (x + 1) 
        primes[0] = primes[1] = False

        # 從 2 開始迭代到 x 的平方根。
        for i in range(2, int(x**0.5) + 1):
            # 如果數字 i 是質數（即 primes[i] 為 True）：
            if primes[i]:
                # 將 i 的所有倍數都標記為非質數，因為它們不能是質數。
                # 從 i*i 開始，因為小於 i 的倍數先前已經被標記過了。
                for j in range(i*i, x + 1, i):
                    primes[j] = False

        # 建立一個包含所有標記為質數（primes[i] 為 True）的數字 i 的列表。
        primes_list = [i for i, is_prime in enumerate(primes) if is_prime]
        return primes_list
    
    def nonSpecialCount(self, l: int, r: int) -> int:
        table=self.sieve_of_eratosthenes(int((r)**0.5))
        tmp=[n for n in table if r >= n**2 >=l]
        return (r-l+1) - len(tmp)
    
sln=Solution()
#sln.sieve_of_eratosthenes(19)
assert 3==sln.nonSpecialCount(l = 5, r = 7)
assert 11==sln.nonSpecialCount(l = 4, r = 16)
        
        