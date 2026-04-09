import numpy as np

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 1_000_000_007
        arr = np.array(nums, dtype=np.int64)
    
        # Delta map for compressed k=1 queries
        delta = {}
    
        for l, r, k, v in queries:
            if v == 1: continue
            if k > 1:
                # Traditional Vectorization for sparse updates
                arr[l : r + 1 : k] = (arr[l : r + 1 : k] * v) % MOD
            else:
                # Compression: Store only the changes (Deltas)
                delta[l] = (delta.get(l, 1) * v) % MOD
                delta[r + 1] = (delta.get(r + 1, 1) * pow(v, MOD - 2, MOD)) % MOD

        # Cumulative Sweep to apply the compressed multipliers
        curr = 1
        # Sorting keys lets us skip empty spaces in the array
        for i in range(n):
            if i in delta:
                curr = (curr * delta[i]) % MOD
            if curr != 1:
                arr[i] = (arr[i] * curr) % MOD

        return int(np.bitwise_xor.reduce(arr))
