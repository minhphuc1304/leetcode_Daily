class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        lastBit = groups[0]
        for i in range(1, len(words)):
            if groups[i] != lastBit:
                res.append(words[i])
                lastBit ^= 1
                
        return res
