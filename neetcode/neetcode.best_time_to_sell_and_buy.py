class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        for i in range (len(prices)):
            for k in range (i, len(prices)):
                    profit= prices[k]-prices[i]
                    profits.append(profit)
        return max(profits)