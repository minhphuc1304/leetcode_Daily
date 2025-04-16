from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        left = 0
        freq = defaultdict(int)
        pair_count = 0
        res = 0
        n = len(nums)

        for right in range(n):
            # Cộng thêm số cặp mới tạo ra khi thêm nums[right]
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1

            # Dịch left lên khi đủ điều kiện
            while pair_count >= k:
                res += (n - right)  # Các subarray từ left đến right, right+1,... là hợp lệ
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]
                left += 1

        return res


nums = [3,1,4,3,2,2,4]
k = 2
print(Solution().countGood(nums, k))  # Output: 4
