class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def helper(r, c, index):
            if r < 0 or c < 0 or r == ROWS  or c == COLS or board[r][c] != word[index] or (r, c) in visit:
                return False
            if index == len(word) - 1:
                return True
            visit.add((r,c))
            if helper(r + 1, c, index + 1) or helper(r - 1, c, index + 1) or helper(r, c + 1, index + 1) or helper(r, c - 1, index + 1):
                return True
            visit.remove((r,c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if helper(r, c, 0):
                        return True
        return False
        