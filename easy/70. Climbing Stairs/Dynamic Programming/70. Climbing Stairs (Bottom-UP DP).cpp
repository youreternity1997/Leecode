// https://leetcode.com/problems/climbing-stairs/solutions/4584184/beats-100-users-c-java-python-javascript-4-approaches-explained/
// Time complexity : O(n)
// Space complexity : O(n)
// Bottom-UP  DP

class Solution {
public:

    int solve(int i, int n, vector<int>& dp) {
        if (i == n) return 1;
        if (i > n) return 0;

        if (dp[i] != -1) return dp[i];

        dp[i] = solve(i + 1, n, dp) + solve(i + 2, n, dp);

        return dp[i];
    }

    int climbStairs(int n) {
        vector<int> dp(n + 1, -1);
        return solve(0, n, dp);
    }
};
