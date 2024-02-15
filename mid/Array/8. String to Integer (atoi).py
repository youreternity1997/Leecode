# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        out = 0
        neg = 1

        symbols = {
            "-":-1,
            "+":1
        }

        left = 0
        while left < len(s) and s[left] == " ":
            left += 1
        
        if left < len(s) and s[left] in symbols:
            neg = symbols[s[left]]
            left += 1

        while left < len(s) and s[left].isdigit():
            out = (out * 10) + int(s[left])
            left += 1

        # bound check
        val = out * neg

        if val >= 2**31 - 1:
            return 2**31 - 1
        elif val <= -2**31:
            return -2**31

        return val