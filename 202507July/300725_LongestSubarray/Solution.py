class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # 1) Find global max
        maxA = nums[0]
        for i in range(1, n):
            if nums[i] > maxA:
                maxA = nums[i]
        
        # 2) Count longest contiguous run where (v & maxA) == maxA
        res = 0
        c = 0
        for i in range(n):
            if (nums[i] & maxA) == maxA:
                c += 1
                if c > res:
                    res = c
            else:
                c = 0
        
        return res
