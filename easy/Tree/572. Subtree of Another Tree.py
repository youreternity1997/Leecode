# https://leetcode.com/problems/subtree-of-another-tree/solutions/4688190/50-1-approach-1-o-n-m-python-c-step-by-step-explanation/
# Time complexity : O(n⋅m),where n is the number of nodes in the root tree and m is the number of nodes in the subRoot tree.
# Space complexity: O(h), where h is the height of the root tree 
# Recursion

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it means any subtree can match, so return True
        if subRoot == None :
            return True

        # If root is None, there are no nodes left in the root tree to check, so return False
        if root == None :
            return False

        # If the subtree rooted at the current node of root matches the subRoot, return True
        if self.same(root , subRoot):
            return True
        
        # Recursively check if subRoot is a subtree of the left or right child of the current node
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

    # Helper function to check if two subtrees are identical
    def same(self , r , s):
        # If both trees are None, they are identical
        if r == None and s == None :
            return True

        # If one tree is None while the other is not, they are not identical
        if r and s and r.val == s.val:
            # Recursively check if the left and right subtrees are identical
            return self.same(r.right , s.right) and self.same(r.left , s.left)  

        # If the values of the current nodes do not match, the trees are not identical
        return False  