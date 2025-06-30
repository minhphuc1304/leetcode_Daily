class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                ans = max(ans, right - left + 1)
        
        return ans
