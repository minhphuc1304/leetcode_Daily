class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        def fn(edges, k): 
            n = len(edges)+1
            tree = [[] for _ in range(n)]
            for u, v in edges: 
                tree[u].append(v)
                tree[v].append(u)
            ans = [0]*n
            for x in range(n): 
                stack = [(x, -1, 0)]
                while stack: 
                    u, p, d = stack.pop()
                    if d <= k: ans[x] += 1
                    for v in tree[u]: 
                        if v != p: 
                            stack.append((v, u, d+1))
            return ans 
        
        most = max(fn(edges2, k-1))
        return [x+most for x in fn(edges1, k)]
