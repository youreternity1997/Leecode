// Time complexity: O(log n)
// Space complexity: O(1)
// Binary Search


class Solution {
public:
    int findMin(vector<int>& nums) {
        int ans = nums[0];
        int low = 0 , high = nums.size()-1;

        if(nums[low] < nums[high]){
            return nums[low];
        }

        // Binary Search:
        while(low <= high){
            if(nums[low] < nums[high]){
                ans = min(ans , nums[low]);
                break;
            }

            int mid = (low + high)/2;
            ans = min(ans , nums[mid]);

            if(nums[mid] >= nums[low]){
                low = mid + 1;
            }
            else{
                high = mid -1 ;
            }
        }
        return ans;
    }
};