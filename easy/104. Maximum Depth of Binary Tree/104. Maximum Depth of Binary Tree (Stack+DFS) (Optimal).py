# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/6090383/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/

# Time Complexity: O(n), where n is the number of nodes. Each node is visited exactly once.
# Space Complexity:
# Recursive: O(h), where h is the height of the tree (call stack).
# Iterative: O(h), where h is the height of the tree (stack storage).

# Edge Cases :
# Empty Tree: root = null → Depth is 0.
# Single Node Tree: root = [1] → Depth is 1.
# Beats 100%

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # Empty Tree: root = null → Depth is 0.
            return 0 
        stack = [(root, 1)] #　Single Node Tree: root = [1] → Depth is 1.
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth