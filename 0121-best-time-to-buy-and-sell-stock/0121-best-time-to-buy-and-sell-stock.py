class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        big = 0

        while r < len(prices) :
            curr = prices[r] - prices[l]

            if prices[l] < prices[r]:
                big = max(big, curr)
            else :
                l = r
            
            r += 1

        print(big)


        return big
