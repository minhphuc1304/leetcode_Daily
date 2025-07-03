class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b > c:
            if a == c:
                return "equilateral"
            elif a == b or b == c:
                return "isosceles"
            else:
                return "scalene"
        return "none"      
