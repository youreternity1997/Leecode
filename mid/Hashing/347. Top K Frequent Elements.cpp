// https://leetcode.com/problems/top-k-frequent-elements/solutions/4580564/5-1-approach-1-o-n-log-n-python-c-step-by-step-explanation/
// Time complexity : O(n log n)
// Space complexity : O(n)
// Hash Map

class Solution {
    static bool cmp(pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second;
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Use an unordered_map (mp) to count the frequency of each element in nums.
        unordered_map<int, int> mp;
        for (auto x : nums) {
            mp[x]++;
        }

        // Step 2: Create a vector of pairs (v) to store the elements and their frequencies.
        vector<pair<int, int>> v;
        for (auto x : mp) {
            v.push_back(pair{x.first, x.second});
        }

        // Step 3: Sort the vector based on frequencies in descending order.
        sort(v.begin(), v.end(), cmp);

        // Step 4: Create a vector (ans) to store the top k frequent elements.
        vector<int> ans;
        for (int i = 0; i < k; i++) {
            auto it = v.begin() + i;
            ans.push_back(it->first);
        }
        return ans;
    }
};
        