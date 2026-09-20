class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0

        for i in range(1, len(prices)):
            if prices[buy] < prices[i]:
                current = prices[i] - prices[buy]
                if current > profit:
                    profit = current
            else:
                buy = i 
        
        return profit



