class Solution:
    def isKRepeatedSubsequence(self, s: str, pattern: str, k: int) -> bool:
        pos = matched = 0
        m = len(pattern)
        for ch in s:
            if ch == pattern[pos]:
                pos += 1
                if pos == m:
                    pos = 0
                    matched += 1
                    if matched == k:
                        return True
        return False
    
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - 97] += 1
        candidates = [chr(i+97) for i in range(25, -1, -1) if freq[i] >= k]

        q = deque(candidates)
        ans = ""

        while q:
            curr = q.popleft()
            if len(curr) > len(ans) or (len(curr) == len(ans) and curr > ans):
                if self.isKRepeatedSubsequence(s, curr, k):
                    ans = curr

            if len(curr) == 7:
                continue
            for ch in candidates:
                nxt = curr + ch
                if self.isKRepeatedSubsequence(s, nxt, k):
                    q.append(nxt)

        return ans    
