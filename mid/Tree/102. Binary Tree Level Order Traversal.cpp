// https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/2008729/o-n-time-beats-99-97-memory-speed-0ms-may-2022/
// Time complexity: O(n)
// Space complexity: O(h)

class Solution {
     public:
        vector<vector<int>> levelOrder(TreeNode* root) {
            if(root==NULL)
               return {};
            vector<vector<int>> ans; 
            queue<TreeNode*> q;
            q.push(root);
            TreeNode *temp;
            int len;
            while(!q.empty()){
               len=q.size();
		       vector<int> v;
               for(int i=0;i<len;i++){
                    temp=q.front();
                    q.pop();
                    v.push_back(temp->val);

                   if(temp->left) q.push(temp->left);
                   if(temp->right) q.push(temp->right);
                }
		        ans.push_back(v);
            }
          return ans;
        }
     };