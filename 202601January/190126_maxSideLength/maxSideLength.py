class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build 2D prefix sum
        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        # Function to check if a square of size k is valid
        def possible(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        pref[i][j]
                        - pref[i - k][j]
                        - pref[i][j - k]
                        + pref[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False

        # Binary search on side length
        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
