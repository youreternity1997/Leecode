// https://leetcode.com/problems/house-robber-ii/solutions/59921/9-lines-0ms-o-1-space-c-solution/
// Time complexity : O(n)
// Space complexity : O(1)
// Space-Optimzed DP

class Solution {
public:
    int rob(vector<int>& nums) {
        // Robbing the first house and skipping the last house. (Rob houses 0 to n - 2;)
        // Robbing the last house and skipping the first house. (Rob houses 1 to n - 1)
        int n = nums.size(); 
        if (n < 2) return n ? nums[0] : 0;
        return max(helper(nums, 0, n - 2), helper(nums, 1, n - 1));
    }

    int helper(vector<int>& nums, int l, int r) {
        int sec_last = 0, last = 0, cur = 0;
        for(int i = l; i <= r; i++) {
            cur = max(last, nums[i] + sec_last);
            sec_last = last;
            last = cur;
        }
        return cur;
    }
};