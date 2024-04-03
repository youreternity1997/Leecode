// Time complexity: O(n)
// Space complexity: O(1)

class Solution {
public:
    bool canJump(vector<int>& nums)
    {
        int length = nums.size();

        int reach = 0;
        for(int i = 0; i < length; i++)
        {
            if(i > reach)
                return false;
            if(reach > length)
                return true;
            reach = max(reach, nums[i] + i);
        }
        return true;
    }
};