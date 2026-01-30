from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], 
                    changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        n = len(source)
        
        # Build transformation costs
        trans_cost = {}
        for o, c, w in zip(original, changed, cost):
            trans_cost[(o, c)] = min(trans_cost.get((o, c), INF), w)
        
        # Get all unique strings
        all_strs = set(original) | set(changed)
        
        # Set identity costs
        for s in all_strs:
            trans_cost[(s, s)] = 0
        
        # Floyd-Warshall
        strs_list = list(all_strs)
        for k in strs_list:
            for i in strs_list:
                if (i, k) not in trans_cost:
                    continue
                for j in strs_list:
                    if (k, j) not in trans_cost:
                        continue
                    new_cost = trans_cost[(i, k)] + trans_cost[(k, j)]
                    if (i, j) not in trans_cost or new_cost < trans_cost[(i, j)]:
                        trans_cost[(i, j)] = new_cost
        
        # Get unique lengths to check (keep all lengths!)
        lengths_to_check = sorted(set(len(s) for s in all_strs))
        
        # DP
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            
            # Check character match first
            if i < n and source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            # Check all transformation lengths
            for l in lengths_to_check:
                if i + l > n:
                    continue
                
                s_sub = source[i:i + l]
                t_sub = target[i:i + l]
                
                # Only check transformations (not direct matches, already handled above)
                if (s_sub, t_sub) in trans_cost:
                    dp[i + l] = min(dp[i + l], dp[i] + trans_cost[(s_sub, t_sub)])
        
        return -1 if dp[n] == INF else dp[n]
