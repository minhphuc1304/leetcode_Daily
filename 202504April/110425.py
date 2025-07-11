
class Solution:
    def countSymetricIntergers(self, low: int, high: int) -> int:

        def is_symmetric(nums: int)-> bool:
            s = str(nums)
            n = len(s)
            if n % 2 != 0:
                return False
            
            half = n//2
            left = sum(int(s[i]) for i in range(half))
            right = sum(int(s[i]) for i in range(half, n))

            return left == right
        
        return sum(1 for x in range(low, high + 1) if is_symmetric(x))

solution = Solution()
low = 1
high = 121212

result = solution.countSymetricIntergers(low, high)
print(result)
