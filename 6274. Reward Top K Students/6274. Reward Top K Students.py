from typing import List
import heapq
class Solution:
  
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = { p:1 for p in positive_feedback}
        negative = { n:1 for n in negative_feedback}  
        scores=[]
        for id, r in zip(student_id, report):
            score=0
            words=r.split(' ')
            for w in words:
                if w in positive:
                    score+=3
                if w in negative:
                    score-=1  
            scores.append( (score, -id))
        scores.sort(reverse=True)
        tmp=[ -s[1]  for s in heapq.nlargest(k, scores, key=lambda s: (s[0], s[1]))]
        return tmp
        
sln=Solution()
assert [239084671,589204657,43871615]==sln.topStudents(["fkeofjpc","qq","iio"]
,["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"]
,["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"]
,[96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263]
,3)
assert [2,1]==sln.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2)
assert [1,2]==sln.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2)
        
               
        
            
            
                    
                
             