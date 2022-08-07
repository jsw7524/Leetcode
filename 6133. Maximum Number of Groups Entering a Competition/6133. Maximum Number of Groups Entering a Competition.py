from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        baseLine=grades[0]
        groupCounter=1
        groupSize=1
        n=1
        grades.pop(0)
        groupSize+=1
        while groupSize <= len(grades):
            tmp=0
            for i in range(groupSize):
                tmp+=grades.pop(0)
            if tmp > baseLine:
                groupCounter+=1
                baseLine=tmp
                groupSize+=1
            else:
                while tmp <= baseLine:
                    tmp+=grades.pop(0)
                    groupSize+=1
                baseLine=tmp
                groupCounter+=1
        if len(grades) >=1:
            return groupCounter+1
        return groupCounter

sln=Solution()
assert 1==sln.maximumGroups(grades = [8,8])
                   
assert 3==sln.maximumGroups(grades = [10,6,12,7,3,5])
            
