class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suf = [''] * n # Precompute min char in suffix s[i:]
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            if s[i] < min_suf[i + 1]:
                min_suf[i] = s[i]
            else:
                min_suf[i] = min_suf[i + 1]

        t, p, i = [], [], 0 # Robot’s buffer, output, index
        while i < n: # Flush t to p if top of t <= min rem char in s
            while t and t[-1] <= min_suf[i]:
                p.append(t.pop())
            t.append(s[i])  # Move next s[i] into t
            i += 1

        while t:  # Once s is exhausted, flush remaining t to p
            p.append(t.pop())

        return ''.join(p)
