# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Unordered Map
# Time : O(n) / Space : O(128)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for index in range(n):
            if s[index] not in charMap or charMap[s[index]] < left:
                charMap[s[index]] = index
                maxLength = max(maxLength, index - left + 1)
            else:
                left = charMap[s[index]] + 1
                charMap[s[index]] = index
        
        return maxLength