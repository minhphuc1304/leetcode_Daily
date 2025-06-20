class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y, ans = 0, 0, 0
        for idx, ch in enumerate(s):
            if ch == 'N': y += 1
            if ch == 'S': y -= 1
            if ch == 'W': x -= 1
            if ch == 'E': x += 1
            ans = max(ans, min(abs(x) + abs(y) + 2 * k, idx + 1))

        return ans
