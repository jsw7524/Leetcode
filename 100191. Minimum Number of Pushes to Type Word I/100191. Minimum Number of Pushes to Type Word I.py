class Solution:
    def minimumPushes(self, word: str) -> int:
        length=len(word)
        times=1
        total=0
        for i in range(1,length+1):
            total+=times           
            if i%8 ==0:
                times+=1
        return total

sln=Solution()
assert 12==sln.minimumPushes(word = "xycdefghij")
assert 5==sln.minimumPushes(word = "abcde")

            
                