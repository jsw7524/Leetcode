import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens=sentence.split(' ')
        counter=0
        
        for token in tokens:
            p=0
            h=0           
            for c in token:
                if c == '!' or c == '.' or c == ',':
                    p+=1
                if c == '-':
                    h+=1
            if p >=2 or h>=2:
                continue            
                                    
            if 1==len(token):
                if token.isalpha() or token == '!' or token == '.' or token == ',' :
                    counter+=1
                    continue
 
            elif 2==len(token):
                x = re.search("^[a-z]([a-z]+)?([,.!]?)$", token)
                if x is None:
                    continue
                counter+=1
 
            elif len(token)>=3:
                x = re.search("^[a-z]([a-z-]+)?[a-z]([,.!]?)$", token)
                if x is None:
                    continue
                counter+=1
            
        return counter

sln=Solution()
assert 3==sln.countValidWords(sentence = "cat and  dog")
assert 0==sln.countValidWords(sentence = "!this  1-s b8d!")     
assert 5==sln.countValidWords(sentence = "alice and  bob are playing stone-game10")    
assert 6==sln.countValidWords(sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") 
assert 3==sln.countValidWords(sentence = "a b c")                
assert 2==sln.countValidWords(sentence = ". !")                


assert 4==sln.countValidWords(sentence = ". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5")                