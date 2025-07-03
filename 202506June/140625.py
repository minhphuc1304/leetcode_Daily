class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        ch = next((c for c in s if c!='9'), None)
        mx = ''.join(('9' if c==ch else c for c in s) if ch else s)
        ch0 = s[0]
        mn = ''.join('0' if c==ch0 else c for c in s)
        return int(mx) - int(mn)
