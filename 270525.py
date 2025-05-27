class Solution(object):
    def differenceOfSums(self, n, m):
        return (1 + n) * n // 2 - (1 + n // m) * (n // m) * m
