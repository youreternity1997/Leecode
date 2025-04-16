# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/565412/detailed-python-walkthrough-from-an-o-n-2-solution-to-o-n-faster-than-99-77/
# T: O(N^2) where N is the number if items in either the preorder or inorder 
# S: O(N^2)
# Beats 51%

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root