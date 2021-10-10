from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym= ''.join([w[0] for w in words])
        return True if s == acronym else False
        