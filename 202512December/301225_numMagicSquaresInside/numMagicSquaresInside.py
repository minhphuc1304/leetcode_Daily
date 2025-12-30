class Solution:
    magicalSquares = {
        (2, 7, 6): (
            (9, 5, 1),
            (4, 3, 8),
        ),
        (2, 9, 4): (
            (7, 5, 3),
            (6, 1, 8),
        ),
        (4, 3, 8): (
            (9, 5, 1),
            (2, 7, 6),
        ),
        (4, 9, 2): (
            (3, 5, 7),
            (8, 1, 6),
        ),
        (6, 1, 8): (
            (7, 5, 3),
            (2, 9, 4),
        ),
        (6, 7, 2): (
            (1, 5, 9),
            (8, 3, 4),
        ),
        (8, 1, 6): (
            (3, 5, 7),
            (4, 9, 2),
        ),
        (8, 3, 4): (
            (1, 5, 9),
            (6, 7, 2),
        )
    }

    def isMagic(self, grid, rowStart, colStart) -> bool:
        firstRow = tuple(grid[rowStart][colStart:colStart+3])
        secondRow = tuple(grid[rowStart+1][colStart:colStart+3])
        thirdRow = tuple(grid[rowStart+2][colStart:colStart+3])

        if firstRow in self.magicalSquares:
            if self.magicalSquares[firstRow][0] == secondRow:
                if self.magicalSquares[firstRow][1] == thirdRow:
                    return True
        
        return False

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m < 3 or n < 3:
            return 0

        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if self.isMagic(grid, i, j):
                    count += 1
        
        return count
