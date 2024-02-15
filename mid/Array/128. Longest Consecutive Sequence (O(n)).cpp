// Time : O(n)
// Space : O(n)

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()<=1)
            return nums.size();
            
        sort(nums.begin(),nums.end());
        int c=1,mx=1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]-nums[i-1]==0)
                continue;
            else if(nums[i]-nums[i-1]==1)
            {
                c++;
                mx=max(mx,c);
            }
            else if(nums[i]-nums[i-1]>1)
            {
                mx=max(mx,c);
                c=1;
            }
        }
        return mx;
    }
};