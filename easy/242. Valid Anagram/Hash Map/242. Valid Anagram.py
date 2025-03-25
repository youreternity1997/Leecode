# https://leetcode.com/problems/valid-anagram/solutions/6072466/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Time Complexity: ( O(n) ) Single pass through both strings.
# Space Complexity: ( O(1) ) Uses a fixed-size array of 26 and a single integer.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {char: s.count(char) for char in set(s)}
        t_dict = {char: t.count(char) for char in set(t)}

        return s_dict == t_dict