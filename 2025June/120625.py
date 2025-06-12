class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m=0 # variable for maximum 
        n=len(nums)
        for i in range(n-1):
            m=max(m,abs(nums[i]-nums[i+1]))
 # taking maximum absolute adjacent difference 
        return max(m,abs(nums[0]-nums[n-1])) 
# also this is circular array diff of last and first elements to check
