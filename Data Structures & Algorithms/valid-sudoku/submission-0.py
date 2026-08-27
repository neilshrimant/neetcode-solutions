class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sqr[(r//3,c//3)]:
                    return False
                
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                sqr[(r//3, c//3)].add(board[r][c])
        return True
        