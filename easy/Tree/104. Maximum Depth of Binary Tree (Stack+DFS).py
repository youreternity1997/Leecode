# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/4254071/depth-first-search-dfs-iterative-approach-o-n-step-by-step-explanation/
# Time: O(N) - number of nodes
# Space: O(h) - for the recursive stack
# Stack + DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root , 1]]
        ans = 0

        while stack:
            node , depth = stack.pop()

            if node:
                ans = max(ans , depth)
                stack.append([node.left , depth+1])
                stack.append([node.right , depth+1])

        return ans  