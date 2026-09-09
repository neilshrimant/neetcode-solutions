class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        pos = [0] * ROWS
        cur_max, cnt = 0, 0

        while True:
            for i in range(ROWS):
                while pos[i] < COLS and mat[i][pos[i]] < cur_max:
                    pos[i] += 1
                if pos[i] >= COLS:
                    return -1
                if mat[i][pos[i]] != cur_max:
                    cnt = 1
                    cur_max = mat[i][pos[i]]
                else:
                    cnt += 1
                    if cnt == ROWS:
                        return cur_max

