class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        countSteer1 = 0
        countCoin1 = 0
        
        while countCoin1 < n:
            countSteer1 += 1
            countCoin1 += countSteer1

        countCoin2 = countCoin1
        countSteer2 = countSteer1
        subCoin = countCoin1 - n

        if subCoin == 0:
            return countSteer1
        else:
            return countSteer1 - 1
