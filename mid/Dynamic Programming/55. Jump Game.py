# Time complexity: O(nk)
# Space complexity: O(n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0] * len(nums)
        dp[0] = True
        
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and nums[j] >= (i-j):
                    dp[i] = True
                    break
        return dp[-1]