class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        # Helper
        def check_hamming_distance(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if cnt == 0:
                        cnt = 1
                    else:
                        return False
            return cnt == 1

        # Initialization
        n = len(words)
        if n == 1:
            return words
        len_dict = {}
        dp = [1] * n
        record = [-1] * n
        for i in range(n):
            l = len(words[i])
            if l in len_dict:
                len_dict[l].append(i)
            else:
                len_dict[l] = [i]
                record[i] = i
        # DP
        longest_len = 0
        longest_ending_index = -1
        for i in range(1,n):
            for j in len_dict[len(words[i])]:
                if j == i:
                    break
                if groups[i] == groups[j] or not check_hamming_distance(words[i], words[j]):
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    record[i] = j
            if dp[i] > longest_len:
                longest_len = dp[i]
                longest_ending_index = i

        # Trace back
        if longest_len == 1:
            return [words[0]]
        res = [None] * longest_len
        off = 1
        while off <= longest_len:
            res[longest_len - off] = words[longest_ending_index]
            off += 1
            longest_ending_index = record[longest_ending_index]
        return res
