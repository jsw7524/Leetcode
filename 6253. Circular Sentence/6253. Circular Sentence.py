class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        for i, w in enumerate(words):
            if words[i-1][-1]!=words[i][0]:
                return False
        return True
    
sln=Solution()
assert False==sln.isCircularSentence(sentence = "Leetcode is cool")
assert True==sln.isCircularSentence(sentence = "eetcode")
assert True==sln.isCircularSentence(sentence = "leetcode exercises sound delightful")
                
        