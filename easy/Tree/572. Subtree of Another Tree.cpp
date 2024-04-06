// https://leetcode.com/problems/subtree-of-another-tree/solutions/4688190/50-1-approach-1-o-n-m-python-c-step-by-step-explanation/
// Time complexity : O(n⋅m),where n is the number of nodes in the root tree and m is the number of nodes in the subRoot tree.
// Space complexity: O(h), where h is the height of the root tree 
// Recursion

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // If subRoot is NULL, any subtree can match, so return true
        if(subRoot == NULL){
            return true;
        }
        // If root is NULL, there are no nodes left in the root tree to check, so return false
        if (root == NULL) {
            return false;
        }
        // If the subtree rooted at the current node of root matches the subRoot, return true
        if (same(root, subRoot)) {
            return true;
        }
        // Recursively check if subRoot is a subtree of the left or right child of the current node
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
private:
    // Helper function to check if two subtrees are identical
    bool same(TreeNode* r, TreeNode* s) {
        // If both trees are NULL, they are identical
        if (r == NULL && s == NULL) {
            return true;
        }
        // If one tree is NULL while the other is not, they are not identical
        if (r == NULL || s == NULL) {
            return false;
        }
        // If the values of the current nodes do not match, the trees are not identical
        if (r->val != s->val) {
            return false;
        }
        // Recursively check if the left and right subtrees are identical
        return same(r->left, s->left) && same(r->right, s->right);
    }
};