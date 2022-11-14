class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        additionalEnergy = 0
        additionalExperience = 0
        n = len(energy)
        for i in range(n):
            opponentEnergy = energy[i]
            opponentExperience = experience[i]
            if initialEnergy <= opponentEnergy:
                needEnergy = (opponentEnergy-initialEnergy)+1
                initialEnergy += needEnergy
                additionalEnergy += needEnergy
            if initialExperience <= opponentExperience:
                needExperience = (opponentExperience-initialExperience)+1
                initialExperience += needExperience
                additionalExperience += needExperience
            initialEnergy -= opponentEnergy
            initialExperience += opponentExperience
        return additionalEnergy + additionalExperience
