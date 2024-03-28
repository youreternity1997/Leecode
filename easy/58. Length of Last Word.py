class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ': # solve the ' '
            i -= 1
        while i >= 0 and s[i] != ' ': # cal length
            length += 1
            i -= 1
        return length