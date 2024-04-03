// https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/3823853/bfs-with-explanation-with-pictures/
// Time  complexity : O(mn)
// Space complexity : O(mn)

struct cell { int row, col; };
class Solution {
public:
    vector<vector<int>> diff = {{0,-1}, {-1,0}, {0,1}, {1,0}};

    void bfs(int row, int col, vector<vector<int>> &heights, queue<cell> &q, vector<vector<bool>> &visited)
    {
        if(visited[row][col]) return;
        q.push({row,col});
        visited[row][col] = true;
        int rows = heights.size(), cols = heights[0].size(), pr, pc, r, c;

        for(int size = q.size(); !q.empty(); size = q.size())
        {
            while(size--)
            {
                pr = q.front().row, pc = q.front().col; q.pop();
                for(auto &d: diff)
                {
                    r = pr + d[0], c = pc + d[1];
                    if(r<0 || r>=rows || c<0 || c>=cols || visited[r][c] || heights[r][c] < heights[pr][pc])
                        continue;
                    visited[r][c] = true;
                    q.push({r,c});
                }
            }
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) 
    {
        int rows = heights.size(), cols = heights[0].size(), lastRow = rows-1, lastCol = cols-1;
        vector<vector<bool>> pacificVisited(rows, vector<bool>(cols)), atlanticVisited = pacificVisited;
        queue<cell> q;

        for(int c=0; c<cols; c++)
            bfs(0, c, heights, q, pacificVisited), bfs(lastRow, c, heights, q, atlanticVisited);
        for(int r=0; r<rows; r++)
            bfs(r, 0, heights, q, pacificVisited), bfs(r, lastCol, heights, q, atlanticVisited);
            
        vector<vector<int>> ans;
        for(int r=0; r<rows; r++) for(int c=0; c<cols; c++) if(pacificVisited[r][c] && atlanticVisited[r][c]) ans.push_back({r,c});
        return ans;
    }
};