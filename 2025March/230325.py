from typing import List
from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build the graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's initialization
        min_heap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        pathCount = [0] * n
        shortest_time[0] = 0
        pathCount[0] = 1

        while min_heap:
            curr_time, u = heapq.heappop(min_heap)

            # Skip if we already found a better time
            if curr_time > shortest_time[u]:
                continue

            for v, t in graph[u]:
                new_time = curr_time + t

                if new_time < shortest_time[v]:
                    shortest_time[v] = new_time
                    pathCount[v] = pathCount[u]
                    heapq.heappush(min_heap, (new_time, v))

                elif new_time == shortest_time[v]:
                    pathCount[v] = (pathCount[v] + pathCount[u]) % MOD

        return pathCount[n - 1] % MOD