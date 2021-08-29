import re
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dictKey={}
        for k in knowledge:
            dictKey[k[0]]=k[1]
            
        result=[]
        state=0
        key=''
        for c in s:
            if '(' == c:
                state=1
                key=''
            elif ')'==c:
                if key in dictKey:
                    result.append(dictKey[key])
                else:
                    result.append("?")                    
                state=0
            else:
                if 1==state:
                    key+=c
                else:
                    result.append(c)
        return ''.join(result)
        
sln=Solution()
assert "bobistwoyearsold"==sln.evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]])
assert "hi?"==sln.evaluate(s = "hi(name)", knowledge = [["a","b"]])
assert "?tzv?r"==sln.evaluate(s = "(fy)(kj)(ege)r", knowledge = [["uxhhkpvp","h"],["nriroroa","m"],["wvhiycvo","z"],["qsmfeing","s"],["hbcyqulf","q"],["xwgfjnrf","b"],["kfipazun","s"],["wnkrtxui","u"],["abwlsese","e"],["iimsmftc","h"],["pafqkquo","v"],["kj","tzv"],["fwwxotcd","t"],["yzgjjwjr","l"]])


