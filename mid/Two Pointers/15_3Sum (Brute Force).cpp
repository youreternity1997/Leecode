// brute force
// Time : O(n^3)
// Space : O(n)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
    sort(begin(nums), end(nums));
    const int n = nums.size();
    set<vector<int>> ans;
    for (int i=0; i<n; ++i)
        for (int j=i+1; j<n; ++j)
            for (int k=j+1; k<n; ++k)
                if ((nums[i]+nums[j]+nums[k]) ==0)
                    ans.insert({nums[i], nums[j], nums[k]});
    return vector<vector<int>>{begin(ans), end(ans)};
    }
};