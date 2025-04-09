# https://leetcode.com/problems/invert-binary-tree/solutions/6082525/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Time Complexity: O(n) Each node is visited once.
# Space Complexity:
# Recursive: O(h), where h is the height of the tree (stack space).
# Iterative: O(w), where w is the maximum width of the tree (queue space).
# Beats 100%

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recurse on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root