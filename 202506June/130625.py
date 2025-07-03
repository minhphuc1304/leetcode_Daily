class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        
        def checkForPairs(diff: int) -> bool:
            count = 0
            i = 1
            n = len(nums)
            while i < n:
                if nums[i] - nums[i - 1] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= p:
                    return True
            return False
            
        left = 0
        right = nums[-1] - nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            if checkForPairs(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left        
