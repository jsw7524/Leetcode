from typing import List

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        record={}
        oneHourInterval=[]
        result=set()
        for ao in sorted([(60*int(at[1][:2])+int(at[1][2:]), at[0]) for at in access_times]):
            if ao[1] not in record:
                record[ao[1]]=0
            record[ao[1]]+=1
            oneHourInterval.append(ao)
            while ao[0]-oneHourInterval[0][0]  >= 60:
                rm=oneHourInterval.pop(0)
                record[rm[1]]-=1
            if  record[ao[1]] >= 3:
                result.add(ao[1])                
        return [r for r in result]
    
sln=Solution()
assert ["akuhmu"]==sln.findHighAccessEmployees(access_times = [["akuhmu","0454"],["aywtqh","0523"],["akuhmu","0518"],["ihhkc","0439"],["ihhkc","0508"],["akuhmu","0529"],["aywtqh","0530"],["aywtqh","0419"]])
assert set(["ab","cd"])==set(sln.findHighAccessEmployees(access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))
assert set(["c","d"])==set(sln.findHighAccessEmployees(access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
assert ["a"]==sln.findHighAccessEmployees(access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])
            
            
        
        