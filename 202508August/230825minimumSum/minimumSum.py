class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def get(a, b, c, d): # inclusive [a, b], [c, d]
            if b < a or d < c:
                return 1e9
            lx, rx, ty, dy = 1e9, -1, 1e9, -1
            for i in range(a, b+1):
                for j in range(c, d+1):
                    if grid[i][j]:
                        lx = min(lx, j)
                        rx = max(rx, j)
                        ty = min(ty, i)
                        dy = max(dy, i)
            return (rx-lx+1) * (dy - ty+1)
        ans = 1e9
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                # type 3
                ans = min(ans, get(0, i, 0, m - 1) + get(i+1, n-1, 0, j) + get(i+1, n-1, j+1, m - 1)) 
                # type 2
                ans = min(ans, get(0, i, 0, j) + get(0, i, j+1, m-1) + get(i+1, n-1, 0, m-1))
                # type 5
                ans = min(ans, get(0, n-1, 0, j) + get(0, i, j+1, m-1) + get(i+1, n-1, j+1, m-1))
                # type 6
                ans = min(ans, get(0, n-1, j+1, m-1) + get(0, i, 0, j) + get(i+1, n-1, 0, j))
        # type 1
        for i in range(n):
            for j in range(i, n):
                ans = min(ans, get(0, i, 0, m-1) + get(i+1, j, 0, m-1) + get(j+1, n-1, 0, m-1))
        # type 4
        for i in range(m):
            for j in range(i, m):
                ans = min(ans, get(0, n-1, 0, i) + get(0, n-1, i+1, j) + get(0, n-1, j+1, m-1))
        return ans
