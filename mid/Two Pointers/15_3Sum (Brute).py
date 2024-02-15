# Brute-force Solution
# Time complexity: O(n^3) 
# Space complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        
        res = []
        for i in ans:
            res += list(i),
        return res