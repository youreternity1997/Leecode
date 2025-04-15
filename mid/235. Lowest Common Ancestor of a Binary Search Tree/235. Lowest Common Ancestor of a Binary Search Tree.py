# Time complexity: O(h) (h is the height of the tree)
# Space complexity: O(1) 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root 
        print('p.val=', p.val)
        print('q.val=', q.val)

        while temp:
            print('temp=', temp)
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif p.val < temp.val and q.val < temp.val:
                temp = temp.left
            else: # p.val <= lowest common ancestor (LCA) <= q.val ; q.val <= LCA <= p.val
                return temp