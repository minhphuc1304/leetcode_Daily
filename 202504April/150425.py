class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
        
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos_in_nums2 = [0] * n
        for i, val in enumerate(nums2):
            pos_in_nums2[val] = i
        
        mapped = [pos_in_nums2[val] for val in nums1]
        
        left_tree = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_tree.query(mapped[i] - 1)
            left_tree.update(mapped[i], 1)
        
        right_tree = FenwickTree(n)
        right_larger = [0] * n
        for i in reversed(range(n)):
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(mapped[i])
            right_tree.update(mapped[i], 1)
        
        return sum(left_smaller[i] * right_larger[i] for i in range(n))
