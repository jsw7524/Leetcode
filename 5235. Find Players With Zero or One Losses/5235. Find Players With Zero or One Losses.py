from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer=[[],[]] 
        dictLoseMatches={}
        for m in matches:
            if m[0] not in dictLoseMatches:
                dictLoseMatches[m[0]]=0
            if m[1] not in dictLoseMatches:
                dictLoseMatches[m[1]]=0
            dictLoseMatches[m[1]]+=1
            
        for id in sorted(dictLoseMatches.keys()):
            if 0==dictLoseMatches[id]:
                answer[0].append(id)
            if 1==dictLoseMatches[id]:
                answer[1].append(id)
                
        return answer

sln=Solution()

assert [[1,2,10],[4,5,7,8]]==sln.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
assert [[1,2,5,6],[]]==sln.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]])

