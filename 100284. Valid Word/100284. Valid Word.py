
class Solution:
    def isValid(self, word: str) -> bool:
        word=word.lower()
        moreThan2 = len(word) > 2
        noWeirds = all(c not in "@#$" for c in word)
        moreThan1Vowel = any(c in "aeiou"  for c in word)
        moreThan1Consonant = any(c in "bcdfghjklmnpqrstvwxyz" for c in word)
        return moreThan2 and noWeirds and moreThan1Vowel and moreThan1Consonant

sln=Solution()
assert False==sln.isValid(word = "UuE6")
assert False==sln.isValid(word = "a3$e")
assert False==sln.isValid(word = "b3")
assert True==sln.isValid(word = "234Adas")