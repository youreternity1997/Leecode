// https://www.youtube.com/watch?v=LupZFfCCbAU
// HarshTable
// Time : O(n*128) / Space : O(128)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int n = s.length();
        int ans = 0;
        for (int i=0; i<n; ++i){
            vector<int> seen(128);
            int j=i;
            while (j<n && !seen[s[j]])
                seen[s[j++]]++;
            ans = max(ans, j-i);
        }
        return ans;
    }
};