// https://bclin.tw/2022/07/06/leetcode-230/
// Time Complexity: O(N)
// Space Complexity: O(N)
// Stack + Iterate

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> node_stack;
        int nodeCount = 0;

        while(true) {
            while(root) {
                node_stack.push(root);
                root = root->left;
            }
            root = node_stack.top();
            nodeCount += 1;
            node_stack.pop();
            if(nodeCount == k){
                break;
            }
            root = root->right;
        }
        return root->val;
    }
};