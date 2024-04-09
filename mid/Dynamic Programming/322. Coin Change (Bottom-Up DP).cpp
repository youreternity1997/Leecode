// https://leetcode.com/problems/coin-change/solutions/4772173/101-1-approach-1-o-n-m-python-c-step-by-step-explanation/
// Time complexity: (O(n * m))
// Space complexity: (O(n))
// Bottiom-Up DP

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Create a vector 'dp' to store the minimum number of coins required for each amount from 0 to 'amount'
        vector<int> dp(amount + 1, amount + 1);
        
        // Base case: Zero coins are required to make amount 0
        dp[0] = 0;
        
        // Iterate through each amount from 1 to 'amount'
        for (int i = 1; i < amount + 1; i++) {
            // Iterate through each coin denomination in 'coins'
            for (int j = 0; j < coins.size(); j++) {
                // Check if the current coin denomination 'coins[j]' can contribute to making up the current amount 'i'
                if (i - coins[j] >= 0) {
                    // Update 'dp[i]' to the minimum of its current value and '1 + dp[i - coins[j]]'
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
        }
        
        // If 'dp[amount]' remains 'amount + 1', it indicates that it's not possible to make up the target amount using the given coin denominations
        if (dp[amount] == amount + 1) {
            return -1;
        }
        // Return the result stored for the target amount 'amount'
        return dp[amount];
    }
};