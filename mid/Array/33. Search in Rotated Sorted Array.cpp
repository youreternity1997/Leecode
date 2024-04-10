// https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/3879263/100-binary-search-easy-video-o-log-n-optimal-solution/
// Time Complexity : O(log⁡n)
// Space Complexity : O(1)
// Binary Search

#include<array> 
#include<iostream>    
#include <vector>

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        return -1;
    }
};

int main() {
    Solution solution;

    // Example 1
    std::vector<int> nums1 = {4, 5, 6, 7, 0, 1, 2};
    int target1 = 0;
    int result1 = solution.search(nums1, target1);
    std::cout << "Example 1: Result = " << result1 << std::endl;

    // Example 2
    std::vector<int> nums2 = {4, 5, 6, 7, 0, 1, 2};
    int target2 = 3;
    int result2 = solution.search(nums2, target2);
    std::cout << "Example 2: Result = " << result2 << std::endl;

    // Add more test cases as needed

    return 0;
}



