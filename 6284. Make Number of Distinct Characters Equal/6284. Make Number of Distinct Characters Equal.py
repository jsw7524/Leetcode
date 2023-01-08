from collections import defaultdict


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1=defaultdict(int)
        w2=defaultdict(int)
        for c in word1:
            w1[c]+=1
        for c in word2:
            w2[c]+=1
        for i in "abcdefghijklmnopqrstuvwxyz":
            for j in "abcdefghijklmnopqrstuvwxyz":
                if w1[i] >= 1 and w2[j] >=1:
                    w1[i]-=1
                    w2[i]+=1
                    w1[j]+=1
                    w2[j]-=1
                    #############
                    if len([ e for e in w1.values() if e >= 1])==len([ e for e in w2.values() if e >= 1]):
                        return True
                    #############
                    w1[i]+=1
                    w2[i]-=1
                    w1[j]-=1
                    w2[j]+=1
        return False

sln=Solution()
assert True==sln.isItPossible(word1 = "abcde", word2 = "fghij")
assert True==sln.isItPossible(word1 = "abcc", word2 = "aab")
assert False==sln.isItPossible(word1 = "ac", word2 = "b")
                    
                