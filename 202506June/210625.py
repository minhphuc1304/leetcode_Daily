class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())

        def numDeletions(current: int) -> int:
            result = 0
            for num in freqs:
                if num < current:
                    result += num
                if num > current + k:
                    result += num - current - k

            return result
        
        return min(map(numDeletions, freqs))
                
