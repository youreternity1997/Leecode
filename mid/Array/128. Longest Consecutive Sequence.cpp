// violent solutions
// Time : O(n*m)
// Space : O(n)

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> h(nums.begin(), nums.end());
        int ans = 0;
        
        for (int num : nums)
            if (!h.count(num - 1)){
                int l = 0;
                while (h.count(num++)) ++l;
                ans = max(ans, l);
            }
        return ans;
    }
};