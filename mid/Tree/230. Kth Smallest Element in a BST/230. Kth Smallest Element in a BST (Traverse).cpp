// https://bclin.tw/2022/07/06/leetcode-230/
// Time Complexity: O(N)
// Space Complexity: O(N)
// Traverse

class Solution {
public:
    vector<int> nums;
    int kthSmallest(TreeNode* root, int k) {
        if(!root) return 0;
        traverse(root);
        return nums[k-1];
    }
    
    void traverse(TreeNode* root) {
        if(!root) return;
        
        traverse(root->left);
        nums.emplace_back(root->val);
        traverse(root->right);
    }
};