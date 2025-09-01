# https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/5816760/o-n-beats-100-sliding-window-java-c-python-go-rust-javascript/
# Time Complexity: O(n)
# Space Complexity: O(1) We use a fixed-size array of 128 integers, regardless of the input size.  O(k)，其中 k 是字元種類數。通常用 ASCII 就是固定的 128，視情況也可能是 256 或 Unicode。

# Hash Map + Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        last_index = {}
        
        start = 0
        for end in range(n):
            current_char = s[end]
            start = max(start, last_index.get(current_char, 0))
            max_length = max(max_length, end - start + 1)
            last_index[current_char] = end + 1
        
        return max_length