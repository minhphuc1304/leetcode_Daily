class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        distance = [[math.inf] * M for _ in range(N)]
        # distance, i, j
        heap = [(0,0,0)]
        while heap:
            # pop the smallest distance from heap
            node = heapq.heappop(heap)
            if node[0] >= distance[node[1]][node[2]]: continue
            if node[1] == N-1 and node[2] == M-1: return node[0]
            # Update distance
            distance[node[1]][node[2]] = node[0]
            for move in moves:
                i,j = node[1] + move[0], node[2] + move[1]
                if not (0 <= i < N and 0 <= j < M): continue
                dist = max(node[0], moveTime[i][j]) + 1
                if dist < distance[i][j]: heapq.heappush(heap, (dist, i, j))
        return -1
                    
        
