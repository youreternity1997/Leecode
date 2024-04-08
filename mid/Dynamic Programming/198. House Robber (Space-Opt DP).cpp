// https://leetcode.com/problems/house-robber/solutions/1605797/c-python-4-simple-solutions-w-explanation-optimization-from-brute-force-to-dp/
// Time complexity : O(n)
// Space complexity : O(n)→O(1)
// Space-Optimzed DP

class Solution {
public:
    int rob(vector<int>& nums) {
        int prev2 = 0, prev = 0, cur = 0;
        for(auto i : nums) {
            cur = max(prev, i + prev2);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
};