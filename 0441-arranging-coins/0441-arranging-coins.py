class Solution:
    def arrangeCoins(self, n: int) -> int:
        countSteer1 = 0
        countCoin1 = 0
        
        while countCoin1 < n:
            countSteer1 += 1
            countCoin1 += countSteer1

        return countSteer1 if (countCoin1 - n) == 0 else countSteer1 - 1
