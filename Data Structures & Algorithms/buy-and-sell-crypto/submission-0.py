class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i<j, max((prices[j] - prices[i]), 0)
        # brute force
        r = 0
        for i in range(len(prices) -1 ):
            for j in range (i+1, len(prices)):
                r = max((prices[j]-prices[i]), r)
        return r

        