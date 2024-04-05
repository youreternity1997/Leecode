# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/4698977/57-1-approach-1-o-n-python-c-step-by-step-explanation/
# Time complexity : O(n)
# Space complexity : O(n) 
# Hashmap + Recursive

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_map = {val: index for index, val in enumerate(inorder)}

        # Define a recursive function to build the binary tree
        def build(pre_start, pre_end, in_start, in_end):
            # it indicates that the current subtree is null, so return None
            if pre_start > pre_end:
                return None

            # Extract the value of the root node from the preorder list using the start index
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find the index of the root node's value in the inorder list using the hashmap
            in_index = inorder_map[root_val]

            # Determine the size of the left subtree
            left_size = in_index - in_start

            # Recursively build the left subtree
            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_index - 1)

            # Recursively build the right subtree
            root.right = build(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

            return root

        # Call the build function with initial parameters corresponding to the entire preorder and inorder lists
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)