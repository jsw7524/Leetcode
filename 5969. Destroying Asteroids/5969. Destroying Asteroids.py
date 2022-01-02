from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a <= mass:
                mass+=a
            else:
                return False
        return True

sln=Solution()
assert True==sln.asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21])
assert False==sln.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4])