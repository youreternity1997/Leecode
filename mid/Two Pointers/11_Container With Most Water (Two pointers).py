# https://leetcode.com/problems/container-with-most-water/solutions/6522099/well-explained-approach-beats-90-runtime/
# Time complexity:O(n)
# Space complexity:O(1)
# Beats 38.33%

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area