# DP
# https://leetcode.com/problems/word-break/solutions/3860456/100-dp-dfs-video-segmenting-a-string/
# Time complexity: ( O(n * m + k) ), where ( n ) is the length of the string, ( m ) is the maximum length of a word in the dictionary, and ( k ) is the total number of characters in all words in the dictionary (for building the Trie).

# Space complexity: ( O(n + k) ), where ( n ) is the length of the string and ( k ) is the total number of characters in all words in the dictionary.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))  # The maximum length of a word in the dictionary

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]