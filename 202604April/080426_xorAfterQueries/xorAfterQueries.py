import numpy as np
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Convert nums to an int64 array to prevent overflow during multiplication
        # before the modulo operation.
        arr = np.array(nums, dtype=np.int64)
        MOD = 10**9 + 7

        for li, ri, ki, vi in queries:
            # Create a slice from li to ri (inclusive) with step ki
            # In NumPy, the stop index is exclusive, so we use ri + 1
            arr[li : ri + 1 : ki] = (arr[li : ri + 1 : ki] * vi) % MOD

        # Perform a bitwise XOR reduction across the entire array
        # np.bitwise_xor.reduce is the vectorized way to XOR all elements
        return int(np.bitwise_xor.reduce(arr))
