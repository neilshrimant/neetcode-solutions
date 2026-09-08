class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS, COLS = len(picture), len(picture[0])
        row_map, col_map = {}, {}
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == "B":
                    row_map[r] = 1 + row_map.get(r, 0)
                    col_map[c] = 1 + col_map.get(c, 0)

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == "B" and row_map[r] == 1 and col_map[c] == 1:
                    res += 1
        
        return res

