# https://leetcode.com/problems/contains-duplicate/solutions/6075376/video-3-solutions-with-sorting-set-and-length/
# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False