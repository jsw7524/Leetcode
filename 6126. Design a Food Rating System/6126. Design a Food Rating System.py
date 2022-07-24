from typing import List

from heapq import nlargest, nsmallest
class foodClass:
    def __init__(self, foodname,cuisineType, rating):
        self.cuisineType=cuisineType
        self.name = foodname
        self.rating = rating
        
    def __lt__ (self, other):
        if self.rating<other.rating:
            return True
        elif self.rating==other.rating:
            if self.name>other.name:
                return True
            else:
                return False
    
class FoodRatings:
 
    def checkHighestRated(self, fcr):
        newone=nlargest(1, self.cuisinesType[fcr.cuisineType] )
        ct=newone[0].cuisineType
        self.cuisinesHighestRated[ct].name=newone[0].name
        self.cuisinesHighestRated[ct].rating=newone[0].rating
        return

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisinesHighestRated={ }
        self.foods={ }
        self.cuisinesType={}
        for f,c,r in zip(foods,cuisines,ratings):
            fcr=foodClass(f,c,r)
            self.foods[f]=fcr
            if c not in self.cuisinesType:
                self.cuisinesType[c]=[]
            
            self.cuisinesType[c].append(fcr)
            
            if c not in self.cuisinesHighestRated:
                self.cuisinesHighestRated[c]=foodClass(f,c,r)
                
            if self.cuisinesHighestRated[c].rating < r:
                self.cuisinesHighestRated[c].name=f
                self.cuisinesHighestRated[c].rating=r
            elif self.cuisinesHighestRated[c].rating == r:
                if f < self.cuisinesHighestRated[c].name:
                    self.cuisinesHighestRated[c].name=f  
                    
        return 
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food].rating=newRating
        self.checkHighestRated(self.foods[food])
        return
        

    def highestRated(self, cuisine: str) -> str:
        tmp=self.cuisinesHighestRated[cuisine].name
        return tmp
    
foodRatings=FoodRatings(["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7])
assert "kimchi"==foodRatings.highestRated("korean"); # return "kimchi"
                                    # "kimchi" is the highest rated korean food with a rating of 9.
assert "ramen"==foodRatings.highestRated("japanese"); # return "ramen"
                                      # "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); # "sushi" now has a rating of 16.
assert "sushi"==foodRatings.highestRated("japanese"); # return "sushi"
                                      # "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); # "ramen" now has a rating of 16.
assert "ramen"==foodRatings.highestRated("japanese"); # return "ramen"
                                      # Both "sushi" and "ramen" have a rating of 16.
                                      # However, "ramen" is lexicographically smaller than "sushi".