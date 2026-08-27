class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruits = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruits += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        time = 0
        directions = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        while q and freshFruits > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
            
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if min(newR, newC) >= 0 and newR < ROWS and newC < COLS and grid[newR][newC] == 1:
                        freshFruits -= 1
                        grid[newR][newC] = 2
                        q.append([newR,newC])
            time += 1
      
        return time if freshFruits == 0 else -1
