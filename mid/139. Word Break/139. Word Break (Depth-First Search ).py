# Depth-First Search
# https://leetcode.com/problems/word-break/solutions/3860456/100-dp-dfs-video-segmenting-a-string/
# Time complexity: ( O(n * m + k) ), where ( n ) is the length of the string, ( m ) is the maximum length of a word in the dictionary, and ( k ) is the total number of characters in all words in the dictionary (for building the Trie).
# Space complexity: ( O(n + k) ), where ( n ) is the length of the string and ( k ) is the total number of characters in all words in the dictionary.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)
    
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if s in wordSet:
            return True
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordSet and self.dfs(s[i:], wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False