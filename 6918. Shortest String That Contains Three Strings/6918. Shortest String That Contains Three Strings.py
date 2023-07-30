class Solution:
    
    def merge(self, a, b):
        if b in a:
            return a
        for i in range(len(a) + 1):
            if b.startswith(a[i:]):
                return a + b[len(a) - i:]
        return a + b
                        
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        result=sorted([
            self.merge(self.merge(a,b),c),
            self.merge(a,self.merge(b,c)),            
            self.merge(self.merge(a,c),b),
            self.merge(a,self.merge(c,b)),            
            self.merge(self.merge(b,a),c),    
            self.merge(b,self.merge(a,c)),    
                                
            self.merge(self.merge(b,c),a),  
            self.merge(b,self.merge(c,a)),    
                                  
            self.merge(self.merge(c,a),b),  
            self.merge(c,self.merge(a,b)),  
                        
                      
            self.merge(self.merge(c,b),a),   
            self.merge(c,self.merge(b,a)),                
                                
        ],key=lambda x: (len(x), x))
        return result[0]

sln=Solution()
assert "cac"==sln.minimumString(a = "a", b = "cac", c = "a")
assert "cab"==sln.minimumString(a = "cab", b = "a", c = "b")
assert "abb"==sln.merge("abb","bb")
assert "abb"==sln.minimumString(a = "bb", b = "bb", c = "a")
assert "ca"==sln.minimumString(a = "ca", b = "a", c = "a")
assert "ac"==sln.merge("a","ac")
assert "a"==sln.merge("a","a")
assert "ac"==sln.minimumString(a = "ac", b = "a", c = "a")
assert "ac"==sln.merge("ac","c")
assert "ab"==sln.merge("ab","b")
assert "ab"==sln.minimumString(a = "a", b = "b", c = "b")
assert "aba"==sln.minimumString(a = "ab", b = "ba", c = "aba")
assert "aaabca"==sln.minimumString(a = "abc", b = "bca", c = "aaa")
assert "aba"==sln.merge("aba","aba")
assert "aaabc"==sln.merge("aaa","abc")
assert "abca"==sln.merge("abc","bca")
assert "aba"==sln.merge("ab","ba")

