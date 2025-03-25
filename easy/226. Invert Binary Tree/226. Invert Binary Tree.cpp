// https://leetcode.com/problems/invert-binary-tree/solutions/664132/python-js-java-go-c-o-n-by-dfs-w-visualization/
// Time complexity: O(N) 
// Space complexity: O(N)
// DFS 

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        
        if( root != nullptr ){
            // invert child node of current root
            swap( root->left, root->right );
            
            // invert subtree with DFS
            invertTree(root->left);
            invertTree(root->right);
            
            return root;
            
        }else{
            // empty tree or empty node
            return nullptr;
        }
    }
};