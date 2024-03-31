// Time complexity: O(V+E)O(V + E)O(V+E)
// Space complexity: O(V+E)O(V + E)O(V+E)

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;
        unordered_set<int> can_take;
        vector<int> prerequisites_count(n, 0);
        vector<vector<int>> reverse_adj(n);
        
        // Create the adjacency lists and reversed adjacency lists
        for (auto pre : prerequisites) {
            reverse_adj[pre[0]].push_back(pre[1]);
            prerequisites_count[pre[1]] += 1;
        }
        
        queue<int> q;
        
        // Enqueue courses with no prerequisites
        for (int i = 0; i < n; i++) {
            if (prerequisites_count[i] == 0) {
                q.push(i);
            }
        }
        
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            can_take.insert(course);
            
            for (auto postreq : reverse_adj[course]) {
                prerequisites_count[postreq] -= 1;
                if (prerequisites_count[postreq] == 0) {
                    q.push(postreq);
                }
            }
        }
        
        if (can_take.size() == n) {
            return true;
        } else {
            return false;
        }
    }
};