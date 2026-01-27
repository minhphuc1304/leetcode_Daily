class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for start, end, weight in edges:
            d[start].append((end, weight))
            d[end].append((start, 2 * weight))

        minheap = [(0, 0)]
        seen = set()
        while minheap:
            score, curr = heappop(minheap)
            if curr == n - 1:
                return score
            
            if curr in seen:
                continue

            seen.add(curr)

            for nei, s in d[curr]:
                if nei not in seen:
                    heappush(minheap, (score + s, nei))
        
        return -1
