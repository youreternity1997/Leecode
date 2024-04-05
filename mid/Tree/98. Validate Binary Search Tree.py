# https://leetcode.com/problems/validate-binary-search-tree/solutions/4285544/recursive-approach-o-n-step-by-step-explanation/
# Time complexity: O(n)
# Space complexity: O(h)
# Recursion

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, min_val=float('-inf'), max_val=float('inf')):
            if root == None:
                return True

            if not (min_val < root.val < max_val):
                return False

            return (bst(root.left, min_val, root.val) and
                    bst(root.right, root.val, max_val))

        return bst(root)