from collections import defaultdict
class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        records=defaultdict(int)
        for word in words:
            hashKey=['0']*26
            for ch in word: 
                hashKey[ord(ch)-ord('a')]='1'
            records[''.join(hashKey)]+=1
        return sum([ v*(v-1)//2 for v in records.values() if v > 1 ])

sln=Solution()
assert 0==sln.similarPairs(words = ["nba","cba","dba"])
assert 3==sln.similarPairs(words = ["aabb","ab","ba"])
assert 2==sln.similarPairs(words = ["aba","aabb","abcd","bac","aabc"])
        
            
            
            