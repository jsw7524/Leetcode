from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[]
        info={}
        for w in words:
            sortedW=''.join(sorted(w))
            if sortedW not in info:
                info.clear()
                result.append(w)
                info[sortedW]=1   
        return result

sln=Solution()
assert ["abba","cd"]==sln.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])
assert ["a","b","c","d","e"]==sln.removeAnagrams(words = ["a","b","c","d","e"])
assert ["a","b","a"]==sln.removeAnagrams(["a","b","a"])  