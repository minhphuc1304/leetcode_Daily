class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        while nums!=sorted(nums):
            min_val =[]
            m =float('inf') 
            for i in range(1,len(nums)):
                min_val.append(nums[i-1]+nums[i])
            m = min(min_val)
            n = min_val.index(m)
            nums[n] = m
            nums.pop(n+1)
            c+=1
        return c
