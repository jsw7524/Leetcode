class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens=s.split(' ')
        numbers=[]
        for t in tokens:
            if t.isnumeric():
                numbers.append(int(t))
        
        for i in range(1,len(numbers)):
            if numbers[i-1] >= numbers[i]:
                return False
        return True
    
sln=Solution()
assert True==sln.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles")
assert False==sln.areNumbersAscending(s =  "hello world 5 x 5")               
assert True==sln.areNumbersAscending(s = "4 5 11 26")               