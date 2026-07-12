class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost=prices[0]
        profit=0
        for i in range(1,len(prices)):
            minCost=min(prices[i],minCost)
            cost=prices[i]
            profit=max(profit,cost-minCost)
        return profit