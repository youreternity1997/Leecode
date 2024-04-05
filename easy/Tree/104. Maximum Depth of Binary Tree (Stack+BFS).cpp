// https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/4254061/breadth-first-search-bfs-iterative-approach-o-n-step-by-step-explanation/
// Time: O(N) - number of nodes
// Space: O(m) - maximum number of nodes at any level
// Stack + BFS

class Solution {
public:
    // BFS-Iterative
    int maxDepth(TreeNode* root) {
        if(root == NULL){
            return 0;
        }

        int level = 0;
        queue<TreeNode*> que;
        que.push(root);

        while(!que.empty()){
            int size = que.size();

            for(int i = 0 ; i < size ; i++){
                TreeNode* temp = que.front();
                que.pop();
                if (temp->left) {
                    que.push(temp->left);
                }
                if (temp->right) {
                    que.push(temp->right);
                }
            }
            level++;
        }
        return level;
        
        
    }
};