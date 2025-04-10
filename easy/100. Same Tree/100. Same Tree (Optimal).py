# https://leetcode.com/problems/same-tree/solutions/4782659/beats-100-users-c-java-python-javascript-explained/
# Time complexity: O(n) (n is the number of nodes in the tree)
# Space complexity: O(h) (h is the height of the tree)
# Beats 100%

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 都是 None：代表這部分樹相同
        if not p and not q:
            return True
        # 2. 其中一個是 None，另一個不是：代表結構不同
        if not p or not q:
            return False
        # 3. 值不同：代表內容不同
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)