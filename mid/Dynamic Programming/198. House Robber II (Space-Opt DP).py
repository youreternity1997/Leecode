# https://leetcode.com/problems/house-robber-ii/solutions/4768883/97-1-approach-1-o-n-python-c-step-by-step-explanation/
# Time complexity : O(n)
# Space complexity : O(1)
# Space-Optimzed DP

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. Robbing the first house and skipping the last house.
        # 2. Robbing the last house and skipping the first house.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        sec_last = last = cur = 0
        for i in nums:
            cur = max(last, sec_last + i)
            sec_last = last
            last = cur
        return cur