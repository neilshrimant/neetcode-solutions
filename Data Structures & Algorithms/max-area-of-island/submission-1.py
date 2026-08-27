class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[0, 1], [0, -1],[1, 0],[-1, 0]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            res = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    res += 1
            return res



        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    area = max(area, bfs(r,c))      
        return area
