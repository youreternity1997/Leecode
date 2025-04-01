# https://leetcode.com/problems/valid-parentheses/solutions/6028416/0-ms-runtime-beats-100-user-step-by-steps-solution-easy-to-understand/
# Time Complexity: (O(n)), where (n) is the length of the string, as each character is pushed and popped from the stack at most once.
# Space Complexity: (O(n)), for storing unmatched opening brackets in the stack.
# Beats 100%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack