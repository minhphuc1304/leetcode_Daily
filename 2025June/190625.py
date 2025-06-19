class Solution:
    def partitionArray(self, a: List[int], k: int) -> int:
        return len({*accumulate(sorted(a),lambda q,v:(q,v)[v-q>k])})
