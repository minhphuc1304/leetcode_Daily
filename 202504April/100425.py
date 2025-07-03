class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, l: int, s: str) -> int:
        cnt = [0] * 16
        def count(n : str, s: str) -> int:
            res, i, sz = cnt[len(n) - 1], 0, len(n) - len(s)
            while True:
                res += n[i:] >= s if i == sz else cnt[len(n) - i - 1] * (min(l, int(n[i]) - 1) + (i > 0))
                i += 1
                if i > sz or int(n[i - 1]) > l:
                    break
            return res            
        for i in range(len(s), 16):
            cnt[i] = 1 if i == len(s) else cnt[i - 1] * (l + 1)
        return count(str(finish), s) - count(str(start - 1), s)