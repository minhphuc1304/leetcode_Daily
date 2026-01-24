class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        max_pair_sum = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > max_pair_sum:
                max_pair_sum = current_sum

            left += 1
            right -= 1

        return max_pair_sum
