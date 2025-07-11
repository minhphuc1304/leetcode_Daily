class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        minHeap = []
        start = 0
        meetings = 0
        day = 0
        while start < n or minHeap:
            if not minHeap:
                day = events[start][0]

            while start < n and events[start][0] <= day:
                heapq.heappush(minHeap, events[start][1])
                start += 1

            if minHeap:
                heapq.heappop(minHeap)
                meetings += 1
                day += 1

            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)

        return meetings
