class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        milage=0
        counter=0
        while mainTank>0:
            mainTank-=1
            milage+=10
            counter+=1
            if counter==5:
                counter=0
                if additionalTank > 0:
                    additionalTank-=1
                    mainTank+=1
        return milage

sln=Solution()
assert 100==sln.distanceTraveled(mainTank = 9, additionalTank = 1)
assert 10==sln.distanceTraveled(mainTank = 1, additionalTank = 2)
assert 60==sln.distanceTraveled(mainTank = 5, additionalTank = 10)
        
                    
            
        