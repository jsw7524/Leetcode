class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_Even=n//2
        n_Odd=n-n_Even
        m_Even=m//2
        m_Odd=m-m_Even
        return n_Even*m_Odd + n_Odd*m_Even
    
sln=Solution()
assert 0==sln.flowerGame(n = 1, m = 1)
assert 3==sln.flowerGame(n = 3, m = 2)
        