# https://leetcode.com/problems/coin-change/solutions/4772173/101-1-approach-1-o-n-m-python-c-step-by-step-explanation/
# Time complexity: (O(n * m))
# Space complexity: (O(n))
# Bottiom-Up DP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a list 'dp' to store the minimum number of coins required for each amount from 0 to 'amount'
        dp = [amount + 1] * (amount + 1)
        
        # Base case: Zero coins are required to make amount 0
        dp[0] = 0

        # Iterate through each amount from 1 to 'amount'
        for a in range(1, amount + 1):
            # Iterate through each coin denomination in 'coins'
            for c in coins:
                # Check if the current coin denomination 'c' can contribute to making up the current amount 'a'
                if a - c >= 0:
                    # Update 'dp[a]' to the minimum of its current value and '1 + dp[a - c]'
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        # Return the result stored for the target amount 'amount'
        return dp[amount] if dp[amount] != amount + 1 else -1