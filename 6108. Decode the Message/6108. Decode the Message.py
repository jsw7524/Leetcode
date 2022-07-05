class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(' ','')
        table={' ':' '}
        i=0
        for k in key:
            if k not in table:
                table[k]=chr(97+i)
                i+=1
        return ''.join(table[c] for c in message)

sln=Solution()
assert "the five boxing wizards jump quickly"==sln.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
assert "this is a secret"==sln.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
        
            
            
        