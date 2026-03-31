class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## greedy approach
        maxP = 0
        b, s = 0, 1
        while s<len(prices):
            if(prices[s] > prices[b]):
                maxP = max(maxP, prices[s] - prices[b])
                s += 1
            else:
                b = s
                s += 1
        return maxP
        