class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]

        events.sort(key = lambda x: x[1])

        for i, (beg, end, val) in enumerate(events):
            prevEnd = bisect_right(events, beg - 1, key = lambda x: x[1])

            for j in range(k):
                take, skip = dp[prevEnd][j] + val, dp[i][j + 1]

                if take > skip: 
                    dp[i + 1][j + 1] = take
                else:
                    dp[i + 1][j + 1] = skip

        return dp[-1][-1]
