import math
class Solution(object):
    
    def solving(self, n):
        if n==4:
            return 4
        if n in self.primeDict:
            return n
        result=0
        tmp=n
        for p in self.primes:
            if p*p > n:
                break
            while tmp%p==0:
                result+=p
                tmp//=p
        if tmp > 1:
            result+=tmp
        return self.solving(result)
        
    def primes_sieve2(self, limit):
        a = [True] * limit                          # Initialize the primality list
        a[0] = a[1] = False
        for (i, isprime) in enumerate(a):
            if isprime:
                for n in range(i*i, limit, i):     # Mark factors non-prime
                    a[n] = False
        return a
    
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        sieve=self.primes_sieve2(1+10**5)
        self.primes=[i for i,p in  enumerate(sieve) if p==True]
        self.primeDict={p:1 for p in self.primes}
        return self.solving(n)
    
sln=Solution()

sln.smallestValue(n = 99954)
assert 373==sln.smallestValue(n = 373)
assert 4==sln.smallestValue(n = 4)
assert 3==sln.smallestValue(n = 3)
assert 5==sln.smallestValue(n = 15)