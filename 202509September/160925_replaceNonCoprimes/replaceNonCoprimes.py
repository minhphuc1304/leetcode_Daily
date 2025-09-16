import math
from typing import List

def agcd(a, b):
    return a * b // math.gcd(a, b)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(i)
            while len(l) > 1 and math.gcd(l[-1], l[-2]) > 1:
                a = l.pop()
                b = l.pop()
                l.append(agcd(a, b))
        return l
