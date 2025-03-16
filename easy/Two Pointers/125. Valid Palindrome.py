# https://leetcode.com/problems/valid-palindrome/solutions/3864359/python-3-two-solutions-beats-99-33ms/
# Time complexity: O(n)
# Space complexity: O(1)
# Beats 80% 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True