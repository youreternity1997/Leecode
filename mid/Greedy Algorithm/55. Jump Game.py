# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        length = len(nums) - 1

        for i in range(len(nums)):
            if i > reach:
                return False
            if reach >= length:
                return True
            reach = max(reach, i + nums[i])
        return reach >= length