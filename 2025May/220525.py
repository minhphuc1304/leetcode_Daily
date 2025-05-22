class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        intervals = sorted(queries, key=lambda x: x[0])
        idx = 0
        avail = []
        active = []
        chosen = 0

        for i in range(n):
            while active and active[0] < i:
                heapq.heappop(active)

            coverage = len(active)
            while idx < m and intervals[idx][0] <= i:
                l, r = intervals[idx]
                heapq.heappush(avail, (-r, r))
                idx += 1

            demand = nums[i]
            while coverage < demand:
                while avail and avail[0][1] < i:
                    heapq.heappop(avail)
                if not avail:
                    return -1
                _, r = heapq.heappop(avail)
                heapq.heappush(active, r)
                chosen += 1
                coverage += 1

        return m - chosen     
