from math import comb
MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # max độ dài chuỗi ta cần xét: log2(maxValue) ~ 14
        maxLen = 14

        # Tiền xử lý tổ hợp C[n][k] = comb(n - 1, k - 1)
        C = [[0] * (maxLen + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, min(i + 1, maxLen + 1)):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        # dp[x][k]: số dãy độ dài k kết thúc bằng x
        dp = [[0] * (maxLen + 1) for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1  # dãy độ dài 1

        for length in range(2, maxLen + 1):
            for i in range(1, maxValue + 1):
                for j in range(2 * i, maxValue + 1, i):
                    dp[j][length] = (dp[j][length] + dp[i][length - 1]) % MOD

        # Tính tổng cho từng độ dài
        result = 0
        for val in range(1, maxValue + 1):
            for length in range(1, maxLen + 1):
                if length <= n:
                    result = (result + dp[val][length] * C[n - 1][length - 1]) % MOD

        return result
