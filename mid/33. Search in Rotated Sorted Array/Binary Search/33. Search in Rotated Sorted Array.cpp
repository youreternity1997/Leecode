#include<array> 
#include<iostream>    
#include <vector>

// https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/3879263/100-binary-search-easy-video-o-log-n-optimal-solution/
// Time Complexity : O(log⁡n)
// Space Complexity : O(1)
// Binary Search

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (nums[mid] == target) { // 剛好中間點就是答案就
                return mid;
            }
            // 左半邊是有序的 (left portion is non-rotated.)
            if (nums[low] <= nums[mid]) { 
                // 如果 target 在左半邊的範圍內，則繼續在左半邊進行搜尋 (search left portion (non-rotated))
                if (target >= nums[low] && target < nums[mid]) {
                    high = mid - 1; // 縮小右邊
                } else { // 否則，轉向右半邊進行搜尋
                    low = mid + 1; // 縮小左邊
                }
            } else { // 否則，則右半邊是有序的 (right portion is non-rotated/ left portion is rotated).
                // 如果 target 在右半邊的範圍內，則繼續在右半邊進行搜尋
                if (target > nums[mid] && target <= nums[high]) {
                    low = mid + 1; 
                } else { // 否則，轉向左半邊進行搜尋
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



