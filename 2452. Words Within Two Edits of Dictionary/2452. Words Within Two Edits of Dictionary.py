from typing import List

class Solution:
    def compareStr(self, a, b):
        diff=0
        for i in range(len(a)):
            if (a[i] != b[i]):
                diff+=1
        return diff
                
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result=[]
        for q in queries:
            for d in dictionary:
                if self.compareStr(q,d)<=2:
                    result.append(q)
                    break
        return result

sln=Solution()
assert ["t","i","m","i","p","s"]==sln.twoEditWords(["t","i","m","i","p","s"],["w","j","b","p","u","b","u","i","h","m"])
assert ["tsl","yyy","rbc","dda","qus","hyb","ilu"]==sln.twoEditWords(queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"], dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"])
assert []==sln.twoEditWords(queries = ["yes"], dictionary = ["not"])
assert ["word","note","wood"]==sln.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"])