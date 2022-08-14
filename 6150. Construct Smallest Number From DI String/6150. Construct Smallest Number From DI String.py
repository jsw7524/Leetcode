class Solution:
    
    def backTracking(self, i, lastDigit):
        if i == self.n:
            self.result=''.join([str(c) for c in self.buffer])
            self.isFound=True
            return 
        else:
            if self.pattern[i] == 'I':
                for d in range(lastDigit+1,10):
                    if 0==self.record[d]:
                        self.record[d]=1
                        self.buffer.append(d)
                        self.backTracking(i+1, d)       
                        if self.isFound:
                            return            
                        self.buffer.pop()
                        self.record[d]=0
            if self.pattern[i] == 'D':
                for d in range(lastDigit-1,0,-1):
                    if 0==self.record[d]:
                        self.record[d]=1
                        self.buffer.append(d)
                        self.backTracking(i+1, d)     
                        if self.isFound:
                            return                  
                        self.buffer.pop()
                        self.record[d]=0
                return 

    def smallestNumber(self, pattern: str) -> str:
        self.pattern='I'+pattern
        self.n=len(pattern)+1
        self.record=[0]*10
        self.buffer=[]
        self.isFound=False
        self.backTracking(0,0)
        return self.result

sln=Solution()

assert "4321567"==sln.smallestNumber(pattern = "DDDIII")
assert "4321"==sln.smallestNumber(pattern = "DDD")
assert "123549876"==sln.smallestNumber(pattern = "IIIDIDDD")
        