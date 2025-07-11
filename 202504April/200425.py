import math
from collections import Counter

class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        res = 0
        
        for x, c in count.items():
            group_size = x + 1
            num_groups = math.ceil(c / group_size)
            res += num_groups * group_size
        
        return res
