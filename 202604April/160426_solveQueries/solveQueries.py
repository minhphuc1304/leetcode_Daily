import bisect
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], q: List[int]) -> List[int]:
        
        mp = {}  # value -> list of indices
        for i, x in enumerate(nums):
            mp.setdefault(x, []).append(i)

        
        for x in mp:
            a = mp[x]
            a.sort()

            # add last at start and first at end (circular handling)
            mp[x] = [a[-1]] + a + [a[0]]

        
        n = len(nums)
        ans = []

        
        for i in q:
            a = mp[nums[i]]

            if len(a) == 3:  # only one occurrence
                ans.append(-1)
                continue

            j = bisect.bisect_left(a, i, 1, len(a)-1)

            l = a[j-1]   # left same value index
            r = a[j+1]   # right same value index
            c = a[j]     # current index

            # d = min circular distance to nearest same value
            d = min(
                abs(c-l), abs(c-r),
                n-abs(c-l), n-abs(c-r)
            )

            ans.append(d)

        return ans

        
