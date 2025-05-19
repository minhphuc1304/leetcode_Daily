class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        from collections import defaultdict

        MOD = 10**9 + 7

        # Step 1: Generate valid column colorings (no two vertical cells same)
        def is_valid(col):
            return all(col[i] != col[i + 1] for i in range(len(col) - 1))

        colors = [0, 1, 2]  # 0 = Red, 1 = Green, 2 = Blue
        valid_cols = []
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        # Step 2: Build mapping of valid transitions (no two horizontal cells same)
        compatible = {}
        for c1 in valid_cols:
            compatible[c1] = []
            for c2 in valid_cols:
                if all(a != b for a, b in zip(c1, c2)):
                    compatible[c1].append(c2)

        # Step 3: Initialize DP table
        dp = defaultdict(int)
        for col in valid_cols:
            dp[col] = 1

        # Step 4: Fill DP table column by column
        for _ in range(1, n):
            new_dp = defaultdict(int)
            for col in valid_cols:
                for prev in compatible[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
