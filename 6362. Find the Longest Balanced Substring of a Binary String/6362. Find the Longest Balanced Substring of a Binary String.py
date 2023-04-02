class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        len0=0
        len1=0
        maxBS=0
        state='part0'
        for i,ch in enumerate(s):
            if state=='part0':
                if ch == '0': 
                    len0+=1
                    len1=0
                else:
                    len1+=1
                    state='part1'
            elif state=='part1':
                if ch == '0':
                    maxBS=max(maxBS,2*min(len0,len1))    
                    len0=1
                    len1=0
                    state='part0'
                else:
                    len1+=1                
        maxBS=max(maxBS,2*min(len0,len1))
        return maxBS

sln=Solution()

assert 2==sln.findTheLongestBalancedSubstring(s = "01011")
assert 4==sln.findTheLongestBalancedSubstring(s = "100111")
assert 4==sln.findTheLongestBalancedSubstring(s = "10011")
assert 0==sln.findTheLongestBalancedSubstring(s = "")
assert 0==sln.findTheLongestBalancedSubstring(s = "111")
assert 4==sln.findTheLongestBalancedSubstring(s = "00111")   
assert 6==sln.findTheLongestBalancedSubstring(s = "01000111")        
                
        
        
        