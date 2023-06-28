class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        pos = 0
        diff = 0

        for n in range(1, len(prices)):
            minValue = min(minValue, prices[n])

            if prices[n-1] > prices[n]:
                pos += 1
            else:
                d = prices[n] - minValue
                diff = max(d,diff)

        if pos == len(prices):
            return 0
        else:
            return diff

        

             
