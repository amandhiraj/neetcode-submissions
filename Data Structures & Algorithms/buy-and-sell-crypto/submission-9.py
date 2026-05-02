class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        max_profit = 0

        for price in prices:
            if price < min_price: #5
                min_price = price
            
            profit = price - min_price #5-1

            if profit > max_profit:
                max_profit = profit
            
        return max_profit
            

            
            

