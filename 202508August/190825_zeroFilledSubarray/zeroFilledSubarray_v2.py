class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        # 1 = 1
        # 2 = 3
        # 3 = 6
        # 4 = 10

        # n ( n+1) / 2

        length_of_zero = 0
        total = 0

        for num in nums:

            if (num == 0):
                length_of_zero += 1
            else:
                if (length_of_zero != 0):
                    total += (length_of_zero * (length_of_zero + 1)) // 2
                    length_of_zero = 0
        
        if (length_of_zero != 0):
            total += (length_of_zero * (length_of_zero + 1)) // 2
        
        return total
