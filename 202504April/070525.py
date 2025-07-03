class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        target, isOdd = divmod(sum(nums), 2)
        if isOdd: return False

        bitmap = 1
        for num in nums: bitmap|= bitmap << num
        
        return bool(bitmap & (1 << target)) 