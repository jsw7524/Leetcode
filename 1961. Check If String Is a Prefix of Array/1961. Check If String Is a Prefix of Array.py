from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        tmp=''
        for i,w in enumerate(words):
            tmp+=w
            if tmp == s:
                return True
        return False

sln=Solution()
assert True==sln.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"])
assert False==sln.isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"])
assert False==sln.isPrefixString(s = "a", words = ["aa","aaaa"])        
assert False==sln.isPrefixString(s = "aaa", words = ["aa","aaaa"])        