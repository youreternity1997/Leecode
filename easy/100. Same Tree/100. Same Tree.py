# https://leetcode.com/problems/same-tree/solutions/4782659/beats-100-users-c-java-python-javascript-explained/
# Time complexity: O(n) (n is the number of nodes in the tree)
# Space complexity: O(h)
# Recursion

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False