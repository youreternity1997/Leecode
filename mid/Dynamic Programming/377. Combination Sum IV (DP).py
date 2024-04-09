# https://leetcode.com/problems/combination-sum-iv/solutions/4020218/98-22-dynamic-programming-recursion-with-memoization/
# Time Complexity: O(N * target).  The outer loop runs target times, and for each iteration, we potentially check all N numbers in nums.
# Space Complexity: O(target). The array dp will have target + 1 elements.
# DP

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]