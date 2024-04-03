# https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/3823853/bfs-with-explanation-with-pictures/
# Time  complexity : O(mn)
# Space complexity : O(mn)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols, lastRow, lastCol = len(heights), len(heights[0]), len(heights)-1, len(heights[0])-1
        pacificVisited, atlanticVisited = [[False] * cols for _ in range(rows)], [[False] * cols for _ in range(rows)]
        q = deque()

        def bfs(row: int, col: int, visited: List[List[bool]]) -> None:
            if visited[row][col]:
                return
            q.append((row, col))
            visited[row][col] = True

            while q:
                for _ in range(len(q)):
                    pr, pc = q.popleft()
                    for (x, y) in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                        r, c = pr + x, pc + y
                        if r<0 or r>=rows or c<0 or c>=cols or visited[r][c] or heights[r][c] < heights[pr][pc]:
                            continue
                        visited[r][c] = True
                        q.append((r, c))
        
        for c in range(cols):
            bfs(0, c, pacificVisited); bfs(lastRow, c, atlanticVisited)
        for r in range(rows):
            bfs(r, 0, pacificVisited); bfs(r, lastCol, atlanticVisited)
        
        return [ [r, c] for r in range(rows) for c in range(cols) if pacificVisited[r][c] == True and atlanticVisited[r][c] == True ]