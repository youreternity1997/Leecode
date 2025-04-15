# https://leetcode.com/problems/validate-binary-search-tree/solutions/6102264/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Time Complexity: O(n), where n is the number of nodes (each node is visited once).
# Space Complexity: O(h), where his the height of the tree (due to recursion stack).
# Beats 100%

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            # Check current node's value against the valid range
            if (min_val is not None and node.val <= min_val) or \
               (max_val is not None and node.val >= max_val):
                return False

            # Recursively validate left and right subtrees
            return validate(node.left, min_val, node.val) and \
                   validate(node.right, node.val, max_val)

        return validate(root, None, None)