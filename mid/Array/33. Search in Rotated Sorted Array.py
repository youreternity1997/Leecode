# https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/3879263/100-binary-search-easy-video-o-log-n-optimal-solution/
# Time Complexity : O(log⁡n)
# Space Complexity : O(1)
# Binary Search

class Solution():
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # left rotated => nums= 4 5 6 7 0 1 2 (mid=7, target=0)
                # in ascending order side
                if nums[left] <= target and target < nums[mid]: # mid=7, target=5, get rid of the right side.
                    right = mid - 1 
                else:
                    left = mid + 1  # mid=7, target=1, get rid of the left side.
                    
            else: # right rotated => nums= 6 7 0 1 2 3 4   (mid=1, target=0)
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1
    
    
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    function = Solution()
    ans = function.search(nums, target)
    print('ans= ', ans)