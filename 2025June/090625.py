class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            steps = self.countSteps(cur, n)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
    
    def countSteps(self, p: int, n: int) -> int:
        steps = 0
        f, l = p, p
        while f <= n:
            steps += min(n + 1, l + 1) - f
            f *= 10
            l = l * 10 + 9
        return steps
