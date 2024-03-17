
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        record={}
        for ch in word:
            if ch not in record:
                record[ch]=0
            record[ch]+=1
        result=10**7
        # one of assumption must be the answer.
        for i in record.keys():
            delOp=0
            for j in record.keys():
                if record[j] >= record[i] :
                    if (record[j] - record[i]) > k:
                        delOp+=(record[j] - record[i])-k
                else:
                    delOp+=record[j]
            result=min(delOp,result)
        return result

sln=Solution()
assert 1==sln.minimumDeletions(word = "aaabaaa", k = 2)
assert 2==sln.minimumDeletions(word = "dabdcbdcdcd", k = 2)
assert 3==sln.minimumDeletions(word = "aabcaba", k = 0)
            
                    
            
            
            