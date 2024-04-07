# https://leetcode.com/problems/climbing-stairs/solutions/4584184/beats-100-users-c-java-python-javascript-4-approaches-explained/
# Time complexity : O(n)
# Space complexity : O(n)
# Bottom-UP  DP


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.solve(0, n, dp)

    def solve(self, i, n, dp):
        if i == n:
            return 1
        if i > n:
            return 0

        if dp[i] != -1:
            return dp[i]

        dp[i] = self.solve(i + 1, n, dp) + self.solve(i + 2, n, dp)

        return dp[i]