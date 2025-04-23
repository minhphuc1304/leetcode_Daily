from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_count = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            group_count[digit_sum] += 1

        max_size = max(group_count.values())
        return sum(1 for size in group_count.values() if size == max_size)
