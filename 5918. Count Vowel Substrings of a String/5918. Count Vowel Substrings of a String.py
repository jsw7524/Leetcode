class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        counter=0
        for f in range(0, len(word)):
            for g in range(f, len(word)):
                a,e,i,o,u=0,0,0,0,0
                for k in range(f, g+1):
                    if word[k] not in "aeiou":
                        a,e,i,o,u=0,0,0,0,0
                        break
                    
                    if word[k] == 'a':
                        a+=1
                    elif word[k] == 'e':
                        e+=1
                    elif word[k] == 'i':
                        i+=1
                    elif word[k] == 'o':
                        o+=1
                    elif word[k] == 'u':
                        u+=1
                if a>=1 and e>=1 and i>=1 and o>=1 and u>=1:
                    counter+=1
        return counter
    
sln=Solution()
assert 7==sln.countVowelSubstrings(word = "cuaieuouac")
assert 2==sln.countVowelSubstrings(word = "aeiouu")
assert 0==sln.countVowelSubstrings(word = "unicornarihan")

assert 0==sln.countVowelSubstrings(word = "bbaeixoubb")