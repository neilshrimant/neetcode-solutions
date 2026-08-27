class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def helper(r,c,grid,visited):
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 1):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visited.add((r,c))
            count = 0
            
            count += helper(r+1,c,grid,visited)
            count += helper(r,c+1,grid,visited)
            count += helper(r-1,c,grid,visited)
            count += helper(r,c-1,grid,visited)

            visited.remove((r,c))
            return count


        return helper(0,0,grid,set())
        