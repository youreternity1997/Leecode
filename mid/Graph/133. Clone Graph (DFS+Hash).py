# https://leetcode.com/problems/clone-graph/solutions/3393494/python-simple-and-clean-beats-94-55/
# Time Complexity : O(N), where N is the number of nodes in the graph and E is the number of edges in the graph.
# Space Complexity : O(N), where N is the number of nodes in the graph. 
# DFS + Stack
# depth-first search (DFS) algorithm to traverse the graph and create the deep copy.

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {}
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.val not in mapping:
                mapping[curr.val] = Node(curr.val)
            if curr.neighbors != []:
                for neighbor in curr.neighbors:
                    if neighbor.val not in mapping:
                        mapping[neighbor.val] = Node(neighbor.val)
                        stack.append(neighbor)
                    mapping[curr.val].neighbors.append(mapping[neighbor.val])
        return mapping[node.val]