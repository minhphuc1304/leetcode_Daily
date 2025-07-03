# Brute force O(n*2)

# class Solution:
#     def countPairs(self, nums: list[int], k: int) -> int:
#         count = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] == nums[j] and (i * j) % k == 0:
#                     count += 1

#         return count

# nums = [3, 1, 2, 2, 2, 1, 3]
# k = 2

# print(Solution().countPairs(nums, k))

# O(nlog(n))

from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        value_to_indices = defaultdict(list)

        for idx, val in enumerate(nums):
            value_to_indices[val].append(idx)

        count = 0

        for indices in value_to_indices.values():
            m = len(indices)
            for i in range(m):
                for j in range(i + 1, m):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count
    
nums = [3,1,2,2,2,1,3]
k = 2
# Output: 4

print(Solution().countPairs(nums, k))