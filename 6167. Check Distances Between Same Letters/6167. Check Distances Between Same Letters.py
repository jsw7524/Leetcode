from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        record={}
        for i, c in enumerate(s):
            if c not in record:
                record[c]=[]
            record[c].append(i)
        for key in record.keys():
            if (record[key][1]-record[key][0]-1)!=distance[ord(key)-ord('a')]:
                return False
        return True

sln=Solution()

assert False==sln.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
assert True==sln.checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])