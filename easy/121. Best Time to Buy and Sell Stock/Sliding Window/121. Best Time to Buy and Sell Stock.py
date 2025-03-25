# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4177821/beats-99-7-o-n-python-step-by-step-explanation/
# Time complexity: O(n), where n is the number of prices
# Space complexity: O(1), as we are using only a constant amount of extra space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, (price - min_price))
        
        return max_profit

            
            