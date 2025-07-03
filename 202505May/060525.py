class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Mã hóa: nhúng nums[nums[i]] vào nums[i]
        for i in range(n):
            nums[i] = nums[i] + n * (nums[nums[i]] % n)
        
        # Giải mã: lấy phần nums[nums[i]]
        for i in range(n):
            nums[i] = nums[i] // n
        
        return nums
