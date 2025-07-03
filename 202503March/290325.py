from typing import List

class Solution:
    MOD = 1000000007

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        upper = max(nums) + 1

        # Compute prime factor counts (primeScore)
        primeScore = [0] * upper
        for i in range(2, upper):
            if primeScore[i] == 0:  # i is prime
                for j in range(i, upper, i):
                    primeScore[j] += 1

        # Monotonic stack for next greater element
        nextGreaterElement = [n] * n
        prevGreaterOrEqualElement = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and primeScore[nums[i]] > primeScore[nums[stack[-1]]]:
                stack.pop()
            prevGreaterOrEqualElement[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and primeScore[nums[i]] >= primeScore[nums[stack[-1]]]:
                stack.pop()
            nextGreaterElement[i] = stack[-1] if stack else n
            stack.append(i)

        # Sort indices based on values in descending order
        sorted_indices = sorted(range(n), key=lambda i: nums[i], reverse=True)

        res = 1
        for idx in sorted_indices:
            num = nums[idx]
            operations = min((idx - prevGreaterOrEqualElement[idx]) * (nextGreaterElement[idx] - idx), k)
            res = (res * pow(num, operations, self.MOD)) % self.MOD
            k -= operations
            if k == 0:
                return res

        return res