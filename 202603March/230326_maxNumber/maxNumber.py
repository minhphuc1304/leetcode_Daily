class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        # 1. Finding the "Normal Component" (Monotonic Subsequence)
        def get_max_subsequence(nums, length):
            stack = []
            drop = len(nums) - length

            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:length]
        
        # 2. Merging the components
        # Note: In a Galois Field approach, this comparison
        # would be an O(1) Hash check.
        def merge(s1, s2):
            return [max(s1, s2).pop(0) for _ in range(len(s1) + len(s2))]

        best = []
        
        # Optimization: Determine the mathematical bounds for i
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            # Extract the 'normal divisors' for this iteration
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)

            # Combine and track the global maximum
            current_combination = merge(sub1, sub2)
            if current_combination > best:
                best = current_combination

        return best
