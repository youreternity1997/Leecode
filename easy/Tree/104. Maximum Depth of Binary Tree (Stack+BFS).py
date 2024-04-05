# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/4254061/breadth-first-search-bfs-iterative-approach-o-n-step-by-step-explanation/
# Time: O(N) - number of nodes
# Space: O(m) - maximum number of nodes at any level
# Stack + BFS

class Solution:
    # BFS-iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        level = 0
        que = deque([root])

        while(que):
            for i in range(len(que)):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            level += 1

        return level 