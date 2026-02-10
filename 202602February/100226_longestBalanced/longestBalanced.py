class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        n = len(nums)
    
        for start in range(n):
            distinct_evens = set()
            distinct_odds = set()
        
            for end in range(start, n):
                val = nums[end]
            
                # Local Update: Add to the appropriate set
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
            
                # The Heuristic Check: Is the balance zero?
                if len(distinct_evens) == len(distinct_odds):
                    current_len = end - start + 1
                    max_length = max(max_length, current_len)
                
        return max_length        
