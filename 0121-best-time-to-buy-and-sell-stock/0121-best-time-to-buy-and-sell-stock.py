class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minCost=prices[0]
        profit=0
        cost=0
        for i in range(1,len(prices)):
            minCost=min(minCost,prices[i])
            cost=prices[i]-minCost
            profit=max(cost,profit)
        return profit
