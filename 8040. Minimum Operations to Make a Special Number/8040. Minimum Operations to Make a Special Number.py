import re
class Solution:
    
    def findRegex(self, regex):
        if regex == None:
            return 99999
        return len(regex[1])+len(regex[2])
    
    def minimumOperations(self, num: str) -> int:
        notZero=len([c for c in num if c != '0'])
        return min(notZero,
                   self.findRegex(re.search("(?P<g0>.*?)0(?P<g1>.*?)0(?P<g2>.*?)", num[::-1])),
                   self.findRegex(re.search("(?P<g0>.*?)5(?P<g1>.*?)2(?P<g2>.*?)", num[::-1])),
                   self.findRegex(re.search("(?P<g0>.*?)0(?P<g1>.*?)5(?P<g2>.*?)", num[::-1])),
                   self.findRegex(re.search("(?P<g0>.*?)5(?P<g1>.*?)7(?P<g2>.*?)", num[::-1])))
    
sln=Solution()
assert 0==sln.minimumOperations(num = "225")
assert 0==sln.minimumOperations(num = "25")
assert 1==sln.minimumOperations(num = "10")
assert 3==sln.minimumOperations(num = "2908305")
assert 2==sln.minimumOperations(num = "2245047")