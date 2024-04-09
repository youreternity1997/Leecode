// https://leetcode.com/problems/combination-sum-iv/solutions/4020218/98-22-dynamic-programming-recursion-with-memoization/
// Time Complexity: O(N * target).  The outer loop runs target times, and for each iteration, we potentially check all N numbers in nums.
// Space Complexity: O(target). The array dp will have target + 1 elements.
// DP

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        std::vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= target; ++i) {
            for (int num : nums) {
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
                }
            }
        }
        
        return dp[target];
    }
};