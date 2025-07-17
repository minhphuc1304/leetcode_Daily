from typing import List
MOD = 10**9 + 7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        
        # Step 1: Run-length encode the input word
        runs = []
        count = 1
        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                runs.append(count)
                count = 1
        runs.append(count)
        
        num_groups = len(runs)
        
        # Step 2: If k > n, it's impossible
        if k > n:
            return 0

        # Step 3: Total combinations without considering the length constraint
        total_combinations = 1
        for run_len in runs:
            total_combinations = (total_combinations * run_len) % MOD

        # Step 4: If even the shortest possible string is ≥ k, return total
        if k <= num_groups:
            return total_combinations

        # Step 5: Count invalid shorter strings and subtract
        extra_chars = k - num_groups
        dp = [0] * extra_chars
        dp[0] = 1

        for run_len in runs:
            max_add = run_len - 1
            new_dp = [0] * extra_chars
            window_sum = 0
            for i in range(extra_chars):
                window_sum = (window_sum + dp[i]) % MOD
                if i > max_add:
                    window_sum = (window_sum - dp[i - max_add - 1]) % MOD
                new_dp[i] = window_sum
            dp = new_dp

        invalid_combinations = sum(dp) % MOD
        return (total_combinations - invalid_combinations + MOD) % MOD
