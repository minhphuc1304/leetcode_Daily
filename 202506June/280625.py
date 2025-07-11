class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted([[num, idx] for idx, num in enumerate(nums)])
        sorted_nums = sorted_nums[-k:]

        return [val for val, _ in sorted(sorted_nums, key = lambda x:x[1])]
