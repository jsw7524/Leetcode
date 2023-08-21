class Solution:
    def makeABC(self, word):
        validABC = [c for c in word]
        nWord = len(word)
        validABC.insert(nWord,"a")
        validABC.insert(0,"c")
        nABC=len(validABC)
        errors=0
        tmp=[]
        for i in range(nABC-1):
            if validABC[i] == 'a':
                tmp.append('a')
                if validABC[i+1] != 'b':
                    tmp.append('b')
                    errors+=1
            if validABC[i] == 'b':
                tmp.append('b')
                if validABC[i+1] != 'c':
                    tmp.append('c') 
                    errors+=1                   
            if validABC[i] == 'c':
                tmp.append('c')
                if validABC[i+1] != 'a':
                    tmp.append('a')
                    errors+=1
        return (errors, tmp[1:])
                
    def addMinimum(self, word: str) -> int:
        errorSum=0
        while (True):
            errors, word=self.makeABC(word)
            if errors==0:
                break
            errorSum+=errors
        return errorSum
        
sln=Solution()
assert 12==sln.addMinimum(word = "cbacba")
assert 2==sln.addMinimum(word =  "b")
assert 6==sln.addMinimum(word =  "aaa")
assert 6==sln.addMinimum(word = "cba")
assert 0==sln.addMinimum(word = "abc")