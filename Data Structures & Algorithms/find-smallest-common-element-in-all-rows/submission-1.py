class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        check_set = defaultdict(set)
    
        for r in range(ROWS):
            for c in range(COLS):
                check_set[mat[r][c]].add(r)
        
        for key, val in check_set.items():
            if len(val) == ROWS:
                return key
            
        return -1

