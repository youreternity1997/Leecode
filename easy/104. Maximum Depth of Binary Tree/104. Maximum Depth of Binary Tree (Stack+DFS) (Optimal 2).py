# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/6299300/beats-super-easy-beginners/

# Time Complexity: O(n), where n is the number of nodes. Each node is visited exactly once.
# Space Complexity:
# Recursive: O(h), where h is the height of the tree (call stack).
# Iterative: O(h), where h is the height of the tree (stack storage).

# Edge Cases :
# Empty Tree: root = null → Depth is 0.
# Single Node Tree: root = [1] → Depth is 1.
# Beats 100%

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.treeHeight(root)

    def treeHeight(self, node: TreeNode) -> int:
        if not node:
            return 0 # Base case: if node is null, return 0

        left_height = self.treeHeight(node.left)   # Get height of left subtree
        right_height = self.treeHeight(node.right) # Get height of right subtree

        return 1 + max(left_height, right_height) # Height of current node