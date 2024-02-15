// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Unordered Map
// Time : O(n) / Space : O(128)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLength = 0;
        unordered_map<char, int> charMap;
        int left = 0;
        
        for (int index = 0; index < n; index++) {
            if (charMap.count(s[index]) == 0 || charMap[s[index]] < left) {
                charMap[s[index]] = index;
                maxLength = max(maxLength, index - left + 1);
            } else {
                left = charMap[s[index]] + 1;
                charMap[s[index]] = index;
            }
        }
        
        return maxLength;
    }
};