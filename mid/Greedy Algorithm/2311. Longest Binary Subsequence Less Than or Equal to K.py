# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/solutions/2168527/python-greedy-fast-easy-to-undestand-with-explanations/
# Time O(n)
# Space O(1)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ones = [i for i, char in enumerate(s[::-1]) if char == '1']
        ans = len(s) - len(ones)
        
        for i in ones:
            if k-2**i < 0:
                break
            k -= 2**i
            ans += 1
        
        return ans