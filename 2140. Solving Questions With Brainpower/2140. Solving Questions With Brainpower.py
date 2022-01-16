from ast import List

class Solution:
    def mostPoints(self, questions) :
        lenQuestions = len(questions)
        dp=[0]*lenQuestions
        dp[-1]=questions[-1][0]
        for i in range(lenQuestions-2,-1,-1):
            if i + questions[i][1] + 1 >= lenQuestions:
                dp[i]=max(questions[i][0] ,dp[i+1])
            else:
                if dp[i+1] > dp[i+questions[i][1] +1] + questions[i][0]:
                    dp[i]=dp[i+1]
                else:
                    dp[i]=dp[i+questions[i][1] +1] + questions[i][0]
        return dp[0]
    
sln=Solution()
assert 79==sln.mostPoints(questions = [[12,46],[78,19],[63,15],[79,62],[13,10]])
assert 7==sln.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]])
assert 5==sln.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]])

