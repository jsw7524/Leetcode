from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result=[]
        for w in words:
            result.extend(w.split(separator))
        return [r for r in result if r !=""]

sln=Solution()
assert []==sln.splitWordsBySeparator(words = ["|||"], separator = "|")
assert ["easy","problem"]==sln.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$")
assert ["one","two","three","four","five","six"]==sln.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = ".")
            
        