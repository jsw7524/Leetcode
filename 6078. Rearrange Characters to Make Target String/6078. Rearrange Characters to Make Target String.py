class Solution:
    # def NumberOfChar(self,s: str, t: str):
    #     counter=0
    #     for c in s:
    #         if c==t:
    #             counter+=1
    #     return counter
        
    
    def rearrangeCharacters(self, s: str, target: str) -> int:
        info={}
        for c in s:
            if c in target:
                if c not in info:
                    info[c]=0
                info[c]+=1
        return min([info[t]//target.count(t) if t in info else 0 for t in target])

sln=Solution()

assert 0==sln.rearrangeCharacters(s = "abc", target = "abcd")
assert 1==sln.rearrangeCharacters(s = "abcba", target = "abc")
assert 1==sln.rearrangeCharacters(s = "abbaccaddaeea", target = "aaaaa")
assert 2==sln.rearrangeCharacters(s = "ilovecodingonleetcode", target = "code")
                