// https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/4254071/depth-first-search-dfs-iterative-approach-o-n-step-by-step-explanation/
// Time: O(N) - number of nodes
// Space: O(h) - the depth of the binary tree, which is h
// Stack + DFS

class Solution {
public:
    int maxDepth(TreeNode* root) {
        stack<pair<TreeNode*, int>> st;
        int ans = 0;
        st.push({root, 1});

        while (!st.empty()) {
            auto [node, depth] = st.top();
            st.pop();

            if (node) {
                ans = max(ans, depth);
                st.push({node->left, depth + 1});
                st.push({node->right, depth + 1});
            }
        }
        return ans;
    }
};