// https://leetcode.com/problems/word-break/solutions/3860456/100-dp-dfs-video-segmenting-a-string/
// Time complexity: ( O(n * m) ), where ( n ) is the length of the string and ( m ) is the maximum length of a word in the dictionary.
// Space complexity: ( O(n) )
// DP 

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        int n = s.size();
        std::vector<bool> dp(n + 1, false);
        dp[0] = true;
        int max_len = 0;
        for (const auto& word : wordDict) {
            max_len = std::max(max_len, static_cast<int>(word.size()));
        }

        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j >= std::max(i - max_len - 1, 0); j--) {
                if (dp[j] && std::find(wordDict.begin(), wordDict.end(), s.substr(j, i - j)) != wordDict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
};