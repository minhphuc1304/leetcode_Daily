# Count Good Triplets
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        length = len(arr)

        for i in range(length):
            for j in range (i + 1,  length):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, length):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1

        return good_triplets
    
    