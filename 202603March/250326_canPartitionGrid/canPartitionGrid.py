class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Try row partition
        rowSums = [sum(row) for row in grid]
        rowTotal = sum(rowSums)
        rowSum = 0
        for r in rowSums[:-1]:
            rowSum += r
            if rowSum == rowTotal - rowSum:
                return True

        # Try col portition
        colSums = [sum([row[c] for row in grid]) for c in range(len(grid[0]))]
        colTotal = sum(colSums)
        colSum = 0

        for c in colSums[:-1]:
            colSum += c
            if colSum == colTotal - colSum:
                return True

        return False
