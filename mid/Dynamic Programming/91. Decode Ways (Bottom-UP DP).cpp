// https://leetcode.com/problems/decode-ways/solutions/1410794/c-python-from-top-down-dp-to-bottom-up-dp-o-1-space-clean-concise/
// Time: O(N), where N <= 100 is length of string s.
// Space: O(N)
// Bottom-up DP


class Solution { // 0 ms, faster than 100.00%
public:
    int numDecodings(const string& s) {
        int n = s.size();
        vector<int> dp(n+1, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] != '0') // Single digit
                dp[i] += dp[i+1];
            if (i+1 < s.size() && (s[i] == '1' || s[i] == '2' && s[i+1] <= '6')) // Two digits
                dp[i] += dp[i+2];
        }
        return dp[0];
    }
};