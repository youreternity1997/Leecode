// https://leetcode.com/problems/maximum-product-subarray/solutions/4402412/0ms-beats-100-rust-python-c-java-simple-dp-solution/
// Time complexity: O(n)  n is the size of the list. 
// Space complexity: O(1)
// DP

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int minProd = nums[0], maxProd = nums[0], ans = nums[0];

        for (auto i = 1; i < nums.size(); i++) {
            int value = nums[i];

            int testMaxProd = maxProd * value;
            int testMinProd = minProd * value;

            maxProd = max({testMaxProd, testMinProd, value});
            minProd = min({testMaxProd, testMinProd, value});

            ans = max(ans, maxProd);
        }

        return ans;
    }
};