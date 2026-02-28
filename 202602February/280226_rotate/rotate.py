class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(i, col):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(row):
            
            left = 0
            right = col - 1

            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
