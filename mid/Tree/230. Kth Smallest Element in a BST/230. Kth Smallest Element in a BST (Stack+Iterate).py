# 
# Time Complexity: O(N)
# Space Complexity: O(H)
# Stack + Iterate
# Beats 100%

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        nodeCount = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nodeCount += 1 
            if nodeCount == k:
                break
            root = root.right
        return root.val