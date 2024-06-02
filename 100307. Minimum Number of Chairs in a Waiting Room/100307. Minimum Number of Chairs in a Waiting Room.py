class Solution:
    def minimumChairs(self, s: str) -> int:
        ppl=0
        chairs=0
        for ch in s:
            if ch=='E':
                ppl+=1
            elif ch=='L':
                ppl-=1
            chairs=max(chairs,ppl)
        return chairs

sln=Solution()
assert 3==sln.minimumChairs(s = "ELEELEELLL")
assert 2==sln.minimumChairs(s = "ELELEEL")
assert 7==sln.minimumChairs(s = "EEEEEEE")
        