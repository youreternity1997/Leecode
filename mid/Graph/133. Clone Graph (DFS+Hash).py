# https://leetcode.com/problems/clone-graph/solutions/3393172/day-98-dfs-hash-table-easiest-beginner-friendly-sol/
# Time Complexity : O(N + E), where N is the number of nodes in the graph and E is the number of edges in the graph.
# Space Complexity : O(N), where N is the number of nodes in the graph. 
# DFS + Hash Table

class Solution:
    def __init__(self):
        self.cloningGraph = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.cloningGraph:
            return self.cloningGraph[node]
        clone = Node(node.val, [])
        self.cloningGraph[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone