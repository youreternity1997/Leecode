# https://leetcode.com/problems/invert-binary-tree/solutions/6082525/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Time Complexity: O(n) Each node is visited once.
# Space Complexity:
# Recursive: O(h), where h is the height of the tree (stack space).
# Iterative: O(w), where w is the maximum width of the tree (queue space).
# Beats 100%

from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Swap left and right children
            node.left, node.right = node.right, node.left

            # Enqueue children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root