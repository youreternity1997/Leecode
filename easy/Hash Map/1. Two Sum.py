# https://leetcode.com/problems/two-sum/solutions/6260615/the-two-sum-moment-beats-100-js-c-py3-java-explanation/
# Time Complexity: O(n), where n is the number of elements in the array. Each number is processed once. Hash map operations (insert and lookup) are (O(1) on average.
# Space Complexity: O(n), as we store up to n numbers in the hash map.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i