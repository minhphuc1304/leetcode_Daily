class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2, z1, z2 = 0, 0, 0, 0
        for x in nums1:
            if x == 0:
                z1 += 1
            else:
                s1 += x
        for x in nums2:
            if x == 0:
                z2 += 1
            else:
                s2 += x

        # Giả sử thay tất cả 0 thành 1
        s1 += z1
        s2 += z2

        # Nếu bên nhỏ hơn không còn 0 để tăng => không thể cân bằng
        if (s1 < s2 and z1 == 0) or (s2 < s1 and z2 == 0):
            return -1

        # Tổng bằng nhau nhỏ nhất có thể đạt được
        return max(s1, s2)
