# https://leetcode.com/problems/number-of-islands/solutions/4731231/easy-dfs-solution-with-explanation-c-java-python-javascript/
# Time complexity : O(n * m)
# Space complexity : (n * m) 
# DFS solution

class Solution:
    def __init__(self):
        self.delRow = [1, -1, 0, 0]
        self.delCol = [0, 0, -1, 1]

    def numIslands(self, grid):
        island = 0
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    island += 1
                    self.dfs(grid, vis, n, m, i, j)
        return island

    def dfs(self, grid, vis, n, m, row, col):
        if row < 0 or row >= n or col < 0 or col >= m or vis[row][col] == 1:
            return

        vis[row][col] = 1

        for i in range(4):
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]

            if 0 <= nRow < n and 0 <= nCol < m and grid[nRow][nCol] == '1' and vis[nRow][nCol] == 0:
                self.dfs(grid, vis, n, m, nRow, nCol)