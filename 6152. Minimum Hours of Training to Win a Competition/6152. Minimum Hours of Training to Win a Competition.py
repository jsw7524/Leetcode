from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        opponentsEnergy=sum(energy)
        opponentsExperience=sum(experience)
        trainingHours=0
        if initialEnergy <= opponentsEnergy:
            trainingHours=1+(opponentsEnergy-initialEnergy)
        bossIndex=experience.index(max(experience))            
        if initialExperience <= (max(experience)-sum(experience[:bossIndex])):
            trainingHours+=(max(experience)-sum(experience[:bossIndex])-initialExperience+1)
        return trainingHours

sln=Solution()

assert 650==sln.minNumberOfHours(initialEnergy = 94, initialExperience = 70, energy = [58,47,100,71,47,6,92,82,35,16,50,15,42,5,2,45,22], experience = [77,83,99,76,75,66,58,84,44,98,70,41,48,7,10,61,28])

assert 51==sln.minNumberOfHours(initialEnergy = 1, initialExperience = 1, energy = [1,1,1,1], experience = [1,1,1,50])
assert 0==sln.minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3])
assert 8==sln.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])
                    