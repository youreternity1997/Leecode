# https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/2008729/o-n-time-beats-99-97-memory-speed-0ms-may-2022/
# Time complexity: O(n)
# Space complexity: O(h)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, ans = deque([root] if root else []), []
        print('queue=', queue)

        while len(queue):
            qlen, row = len(queue), []
            print('qlen==========', qlen)
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
                print('curr=', curr)
                print('curr.val=', curr.val)
                print('curr.left=', curr.left)
                print('curr.right=', curr.right)
                
            ans.append(row)
            print('-----------------------------------------------')
        return ans  