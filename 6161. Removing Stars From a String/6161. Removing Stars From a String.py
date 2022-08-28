class Solution:
    def removeStars(self, s: str) -> str:
        counter=0
        answer=[]
        for c in s[::-1]:
            if c=='*':
                counter+=1
            else:
                if counter > 0:
                    counter-=1
                    continue
                else:
                    answer.append(c)
        return ''.join(answer[::-1])

sln=Solution()
assert ""==sln.removeStars(s = "erase*****")
assert "lecoe"==sln.removeStars(s = "leet**cod*e")
                    
                    
            