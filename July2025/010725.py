class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1 
        i, n = 0, len(word)

        while i < n:
            j = i
            while j < n and word[j] == word[i]:xq
                j += 1
            ans += (j - i - 1)
            i = j
        return ans
