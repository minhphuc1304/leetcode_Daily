class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def maxSpan(bars: list[int]) -> int:
            bars.sort()
            res = 1
            streak = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    streak += 1
                    continue

                res = max(res, streak + 1)
                streak = 1

            return max(res, streak + 1)


        return min(maxSpan(hBars), maxSpan(vBars)) ** 2
