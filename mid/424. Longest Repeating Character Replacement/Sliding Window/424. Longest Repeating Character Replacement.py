# https://leetcode.com/problems/longest-repeating-character-replacement/solutions/5178107/python-beat-90-optimal-solution-full-explanation/
# Sliding Window + HashMap
# Time complexity: O(n)
# Space complexity: O(m) where m is the size of the character set (in this case, the maximum size is 128 for ASCII characters). 
#

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = r = maxlen = maxfre = 0
        hsh = {}
        while (r < len (s)):
            if s[r] in hsh:    
                hsh[ s[r] ] += 1
            else:
                hsh [ s[r]] = 1
            maxfre = max(maxfre, hsh[ s[r]])
            if (r-l+1 - maxfre > k ):
                hsh[s[l]] -= 1

                l += 1 
            else:
                maxlen = max(r-l+1, maxlen)
            
            r += 1
        return maxlen
        