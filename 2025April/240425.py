class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        from collections import Counter

        total_unique = len(set(nums))
        res = 0
        freq = Counter()
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            while len(freq) == total_unique:
                # Với mỗi left thỏa mãn, có (n - right) đoạn con hợp lệ
                res += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
                
        return res