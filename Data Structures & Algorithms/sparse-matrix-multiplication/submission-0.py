class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat1), len(mat2[0])
        res = [[0] * cols for _ in range(rows)]
        
        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        res[row_index][col_index] += row_element * col_element
        
        return res