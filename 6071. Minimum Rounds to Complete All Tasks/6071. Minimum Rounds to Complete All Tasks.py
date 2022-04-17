from typing import List

class Solution:
    def MakeDP(self):
        self.dp=[0]*(1+10**5)
        self.dp[0]=-1
        self.dp[1]=-1
        self.dp[2]=1
        self.dp[3]=1
        self.dp[4]=2
        for i in range(5,1+10**5):
            self.dp[i]=1+min(self.dp[i-2],self.dp[i-3])
        return 
    def minimumRounds(self, tasks: List[int]) -> int:
        self.MakeDP()
        info={}
        for t in tasks:
            if t not in info:
                info[t]=0
            info[t]+=1
        answer=0
        for t in info.keys():
            if 1 == info[t]:
                return -1
            answer+=self.dp[info[t]]
        return answer
    
sln=Solution()
assert 2==sln.minimumRounds(tasks = [5,5,5,5])     
assert 4==sln.minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4])
assert -1==sln.minimumRounds(tasks = [2,3,3])                

        