# https://leetcode.com/problems/house-robber/solutions/1605797/c-python-4-simple-solutions-w-explanation-optimization-from-brute-force-to-dp/
# Time complexity : O(n)
# Space complexity : O(n)→O(1)
# Space-Optimzed DP

class Solution:
    def rob(self, nums: List[int]) -> int:
        sec_last = last = cur  = 0
        for i in nums:
            cur = max(last, sec_last + i)
            sec_last = last
            last = cur
        return cur