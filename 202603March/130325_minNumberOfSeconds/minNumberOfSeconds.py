class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        priority_queue = []

        for time in workerTimes:
            heappush(priority_queue, (time, time, 1))

        ans = 0
        for _ in range(mountainHeight):
            currentTime, originalTime, iteration = heappop(priority_queue)
            ans = currentTime

            heappush(priority_queue, (currentTime + originalTime * (iteration + 1), originalTime, iteration + 1))

        return ans
