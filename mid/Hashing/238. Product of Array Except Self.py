# https://leetcode.com/problems/product-of-array-except-self/solutions/3231758/238-time-96-95-solution-with-step-by-step-explanation/
# time complexity O(n)
# space complexity to O(1) 
# Beats 53.45%

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    # calculate the product of elements to the left of each element and store in result
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # calculate the product of elements to the right of each element and update result
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result