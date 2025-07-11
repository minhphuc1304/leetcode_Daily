from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        def adj(node):
            i,j = node
            res = []
            adj = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
            if 0<=i+1<n:
                res.append((adj[0], moveTime[i+1][j]))
            if 0<=j+1<m:
                res.append((adj[1], moveTime[i][j+1]))
            if 0<=i-1<n:
                res.append((adj[2], moveTime[i-1][j]))
            if 0<=j-1<m:
                res.append((adj[3], moveTime[i][j-1]))
            return res
        
        visited = set()
        pq = []
        pq.append((0,(0,0),0))
        minDist = float('inf')
        while pq:
            w,nde,steps = heappop(pq)
            if nde in visited:
                continue
            else:
                visited.add(nde)
            if nde == (n-1, m-1):
                minDist = min(minDist, w)

            for nbr,nw in adj(nde):
                if nbr not in visited:
                    if steps%2==0:
                        time = w+max(nw-w,0)+1
                    else:
                        time = w+max(nw-w,0)+2
                    heappush(pq, (time,nbr,steps+1))
        
        return minDist
