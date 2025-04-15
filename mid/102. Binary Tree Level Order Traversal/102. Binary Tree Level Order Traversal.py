# https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/5394346/best-approach-is-here-beats-100/
# Time complexity: (O(n)) where (n) is the number of nodes in the tree.
# Space complexity: (O(n)) The space required for the result list ans is proportional to the number of nodes. The queue can hold at most the number of nodes at the largest level, which in the worst case can be (O(n)).
# Beats 100%

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level)
        
        return ans