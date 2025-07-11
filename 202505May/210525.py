class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = any(matrix[0][y] == 0 for y in range(cols))
        first_col_has_zero = any(matrix[x][0] == 0 for x in range(rows))

        for x in range(1, rows):
            for y in range(1, cols):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        for x in range(1, rows):
            if matrix[x][0] == 0:
                for y in range(cols):
                    matrix[x][y] = 0

        for y in range(1, cols):
            if matrix[0][y] == 0:
                for x in range(rows):
                    matrix[x][y] = 0

        if first_row_has_zero:
            for y in range(cols):
                matrix[0][y] = 0

        if first_col_has_zero:
            for x in range(rows):
                matrix[x][0] = 0
