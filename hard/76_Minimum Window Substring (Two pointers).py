# Two Pointer + Sliding Window
# O(m+n)
# O(m+n)
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        answer_key = Counter(t)
        window = {}
        
        valid_keys_required = len(answer_key)
        valid_keys_formed = 0

        output = float('inf'), 0, 0 
        l, r = 0, 0

        # Keep expanding the window until we find a valid substring
        while r < len(s):
            char = s[r] 
            window[char] = window.get(char, 0) + 1 

            if char in answer_key and window[char] == answer_key[char]:
                valid_keys_formed += 1

            while l <= r and valid_keys_formed == valid_keys_required:
                prev_char = s[l]

                # Make sure to update the value of output before incrementing "l"
                if output[0] > (r-l+1):
                    output = (r-l+1), l, r
                
                window[prev_char] -= 1

                if prev_char in answer_key and window[prev_char] < answer_key[prev_char]:
                    valid_keys_formed -= 1
                
                l += 1
            
            r += 1
        
        
        return "" if output[0] == float('inf') else s[output[1]:output[2]+1]