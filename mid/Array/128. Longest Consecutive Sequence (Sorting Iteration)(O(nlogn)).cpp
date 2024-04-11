// https://leetcode.com/problems/longest-consecutive-sequence/solutions/3171985/best-c-4-solution-hash-table-sorting-brute-force-optimize-one-stop-solution/
// Time : O(NlogN)
// Space : O(1)
// Sorting || Iteration

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size()<=1)
            return nums.size();
        sort(nums.begin(), nums.end());
        int count=1, Max=1;
        
        for (int i=1; i<nums.size(); i++)
        {
            if (nums[i]-nums[i-1]==0)
                continue;
            else if (nums[i]-nums[i-1]==1)
            {
                count++;
                Max = max(Max, count);
            }
            else if (nums[i]-nums[i-1]>1)
            {
                Max = max(Max, count);
                count=1;
            } 
        }
        return Max;
    }
};

