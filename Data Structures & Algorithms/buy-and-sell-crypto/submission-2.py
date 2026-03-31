class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowestP = prices[0]
        for i in range(1, len(prices)):
            if prices[i]< lowestP:
                lowestP = prices[i]
            else:
                maxP = max(maxP, prices[i] - lowestP)
        return maxP      