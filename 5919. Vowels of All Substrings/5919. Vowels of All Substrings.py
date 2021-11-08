class Solution:
    def countVowels(self, word: str) -> int:
        wLen=len(word)
        counter=0
        for i in range(wLen):
            if word[i] in 'aeiou':
                counter+=(i+1)*(wLen-i)
        return counter
                 
sln=Solution()
assert 6==sln.countVowels(word = "aba")
assert 3==sln.countVowels(word = "abc")            
assert 0==sln.countVowels(word = "ltcd")
assert 237==sln.countVowels(word = "noosabasboosa")
assert 1==sln.countVowels(word = "a")