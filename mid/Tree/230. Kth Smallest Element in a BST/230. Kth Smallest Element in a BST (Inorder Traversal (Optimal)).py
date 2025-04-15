# https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/6424225/beats-100-c-python-super-simple-and-efficient-solution-python-c/
# Time complexity: O(n)
# Space complexity: O(h) 最壞情況:h=n, O(n); 平衡情況:h=log n, O(log n)
# Beats 100%

class Solution:
  def kthSmallest(self, root: TreeNode | None, k: int) -> int:
    rank = 0          # 紀錄目前是第幾個走訪的節點
    ans = 0           # 儲存答案：第 k 小的節點值

    def traverse(root: TreeNode | None) -> None:
      nonlocal rank, ans
      
      if not root:
        return

      # 左子樹
      traverse(root.left)

      # 中間（目前節點）
      rank += 1
      if rank == k:
        ans = root.val
        return

      # 右子樹
      traverse(root.right)

    # 從 root 開始走訪
    traverse(root)
    return ans