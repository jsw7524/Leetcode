class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dicS={ c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        dicT={ c:0 for c in "abcdefghijklmnopqrstuvwxyz"}        
        
        for c in s:
            dicS[c]+=1
        
        for c in t:
            dicT[c]+=1
            
        commonChars=0    
        for c in "abcdefghijklmnopqrstuvwxyz":
            commonChars+=min(dicS[c],dicT[c])           
        return len(s) + len(t) - 2*commonChars
    
sln=Solution()
assert 7==sln.minSteps(s = "leetcode", t = "coats")
assert 0==sln.minSteps(s = "night", t = "thing")