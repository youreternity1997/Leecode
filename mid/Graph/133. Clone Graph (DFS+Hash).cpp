// https://leetcode.com/problems/clone-graph/solutions/3393172/day-98-dfs-hash-table-easiest-beginner-friendly-sol/
// Time Complexity : O(N + E), where N is the number of nodes in the graph and E is the number of edges in the graph.
// Space Complexity : O(N), where N is the number of nodes in the graph. 
// DFS + Hash Table

class Solution {
public:
    unordered_map<Node*, Node*> cloningGraph;
    
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }
        if (cloningGraph.find(node) == cloningGraph.end()) {
            cloningGraph[node] = new Node(node -> val);
            for (auto neighbor : node -> neighbors) {
                cloningGraph[node] -> neighbors.push_back(cloneGraph(neighbor));
            }
        }
        return cloningGraph[node];
    }
};