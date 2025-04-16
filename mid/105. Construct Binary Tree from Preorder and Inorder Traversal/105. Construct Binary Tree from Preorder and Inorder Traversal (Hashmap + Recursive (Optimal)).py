# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/3451834/simple-python-solution-beats-98-9-and-memory-beats-86-31/
# Time complexity: O(n)
# Space complexity: O(n) Because of recursion and dictionary
# Beats 100%

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.root_index = {}
        self.index = 0
        for i,num in enumerate(inorder):
            self.root_index[num] = i
        
        def construct(left,right):
            if left > right:
                return None
            root = preorder[self.index]
            i = self.root_index[root]
            self.index += 1
            head = TreeNode(root)
            head.left = construct(left,i - 1)
            head.right = construct(i + 1, right)
            return head
        
        n = len(preorder) - 1
        return construct(0,n)